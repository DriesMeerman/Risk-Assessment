import arrow
import traceback

from models import *
from helpers.util import print_seconds_humanized, now_timestring
from helpers.model_saver import ModelContainer
from services.text_processing_service import *

ALL_SINGLE_MODELS = [KNNModelTest, NBModelTest, MultinominalNBModelTest, DTModelTest, SVCModelTest, SGDModelTest,
                     MLPModelTest]
FAST_SINGLE_MODELS = [NBModelTest, DTModelTest,
                      MultinominalNBModelTest]  # Single model which trains faster than the others
ALL_ENSEMBLE_MODELS = [RandomForrestModelTest, AdaBoostModelTest, BaggingModelTest, StackingModelTest,
                       GradientBoostModelTest]
FAST_ENSEMBLE_MODELS = [RandomForrestModelTest, AdaBoostModelTest]


def load_ml_processor() -> MLTextProcessingHelper:
    return MLTextProcessingHelper()


def ml_pre_process(df: pd.DataFrame, config, variation, logger):
    preprocess_columns = config.get_ml_preprocess_columns(variation)

    if len(preprocess_columns) == 0:
        logger.info(f"No preprocess fields found returning df {variation}")
        return df

    logger.info(f"Preprocessing for {variation}, looking at {preprocess_columns}")

    text_pre_processor = load_ml_processor()
    frame = df.copy()

    for col in preprocess_columns:
        frame[col].replace(np.nan, '', regex=True, inplace=True)

    frame = text_pre_processor.add_ml_generated_cols_to_df(frame, preprocess_columns, config)
    return frame


def compare_models(config: ConfigHelper, variation: str, model_classes: List[ModelTest], logger=Logger()):
    start_time = time.time()
    a_start = arrow.now()
    model_containers = []
    model_df = pd.DataFrame()  # columns=['Name', 'Accuracy'])

    dataframe = config.dataframe
    text_columns = set(config.get_vector_columns(variation) + config.get_ml_preprocess_columns(variation))

    # drop invalid rows
    for col in text_columns:
        dataframe = dataframe[dataframe[col].notna()]

    # create cached version of simplified text
    standardizer = None
    topicAnalysers = {}
    if config.standardize_text:
        logger.info("Standardizing text columns: ", text_columns)
        standardizer = TextStandardizer()
        for col in text_columns:
            # https://stackoverflow.com/questions/16236684/apply-pandas-function-to-column-to-create-multiple-new-columns
            dataframe[f"{col}_raw"] = dataframe[col]

            dataframe[col + "_joined"] = dataframe.apply(lambda row: standardizer.standardize(row[col]), axis=1)
            dataframe[col] = dataframe.apply(lambda row: row[col + "_joined"][0], axis=1)
            dataframe[f"{col}_stopword_count"] = dataframe.apply(lambda row: row[col + "_joined"][1], axis=1)
            dataframe.drop(col + "_joined", axis=1, inplace=True)

    if config.lda_topic_generation:
        for col in text_columns:
            texts = dataframe[col].values.tolist()
            topicAnalyser = TopicAnalyzer(texts)
            topicAnalyser.setup()
            topicAnalysers[col] = topicAnalyser

            for i, row in dataframe.iterrows():
                topics, dominant_topic, dominant_topic_value, topic_probability_scores = topicAnalyser.predict(row[col])
                dataframe.at[i, f"_lda_{col}_dominant_topic"] = dominant_topic  # as key word
                dataframe.at[i, f"_lda_{col}_topics"] = ",".join(topics)
                for index, val in enumerate(topic_probability_scores):
                    topic_field = f"_lda_{col}_topic_{index}"
                    dataframe.at[i, topic_field] = val
                    if i == 0:
                        config.configs[variation]['x_cols'].append(topic_field)

    if config.standardize_text:
        logger.csv(dataframe, f"text_standardized_{variation}.csv")

    logger.info(f"## {variation}")
    logger.info(f"Start comparing {a_start.format()}")

    if not config.configs[variation]["ml_cached"]:
        logger.info("Using non cached frame with columns: ", dataframe.columns)
        dataframe = ml_pre_process(dataframe, config, variation, logger)
        logger.info("Extracted columns from non cached frame: ", dataframe.columns)
        logger.csv(dataframe, f"ml_processed_{variation}.csv")
    else:
        logger.info("Using cached frame with columns: ", dataframe.columns)

    for model_class in model_classes:
        model = None
        try:
            model = model_class.get_model(dataframe, config, variation)
            logger.info("### Working on {} -- {} [{}]".format(model.name, variation, now_timestring()))
            logger.info("Using columns: ", config.configs[variation]['x_cols'])
            class_start = time.time()
            model.optimize_config()
            class_duration = time.time() - class_start

            row = {
                'Name': model.name,
                'Accuracy': model.accuracy,
                'Time': model.best_mean_fit_time,
                'Optimization_time': class_duration
            }
            model_df = model_df.append(row, ignore_index=True)

            result = ModelContainer(model.name, model.get_description(), model.model, model.columns,
                                    model.scaler, model.vectorizers, config, variation, model.accuracy,
                                    model.accuracy_train, model.accuracy_test, model.accuracy_val,
                                    model.best_mean_fit_time,
                                    standardizer, topicAnalysers, model.encoders)

            model_containers.append(result)
            logger.info("\n-------------------------------------  \n\n")
        except BaseException as error:
            model_name = model.name if model is not None else str(model_class)
            msg = f"Something went wrong while handling {model_name}\n{str(error)}"
            print(msg)
            logger.error(msg)
            print(traceback.format_exc())
            logger.error(traceback.format_exc())

    logger.info(f"Finished comparing {arrow.now().format()}")
    duration = time.time() - start_time
    print_seconds_humanized(duration, logger)
    best_row = model_df.sort_values(by=['Accuracy'], ascending=False).head(1)
    best_index = best_row.index[0]

    return model_df, model_containers, model_containers[best_index]


def display_model_comparison(model_df, variation, logger: Logger):
    logger.df(model_df.sort_values(by=['accuracy_overall'], ascending=False))
    visual = model_df[['name', 'accuracy_overall']]
    cm = sns.light_palette("green", as_cmap=True)
    model_df.style.background_gradient(cmap=cm)
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.set(style="whitegrid")
    sns.barplot(y='name', x="accuracy_overall", data=visual, ax=ax)
    seconds = round(round(time.time()))
    filename = f"{variation}_comparison_{seconds}"
    logger.log_img(filename)


# variation visualisations
class VariationVisualizer:
    def __init__(self, dataframe: pd.DataFrame, logger: Logger, base_name="overall_"):
        self.logger = logger
        self.base_name = base_name
        self.frame = dataframe

    def display_accuracy_over_variation(self):
        self.logger.info("Image for accuracy over variation")
        fig, ax = plt.subplots(figsize=(16, 8))
        _ = sns.lineplot(data=self.frame, x="variation", y="accuracy_overall", ax=ax)
        plt.xticks(rotation=90)
        self.logger.log_img(self.base_name + "acc_over_variation")

    def display_acc_over_time(self):
        self.logger.info("Accuracy over time")
        fig, ax = plt.subplots(figsize=(16, 8))
        _ = sns.lineplot(data=self.frame, x="fit_time", y="accuracy_overall", ax=ax)
        self.logger.log_img(self.base_name + "acc_over_time")

    def display_acc_over_col_per_variation(self):
        self.logger.info("Acc over colcount for feature variation ")
        fig, ax = plt.subplots(figsize=(16, 8))
        bonk = self.frame[['column_count', 'accuracy_overall', 'name', 'variation']]

        barplot = sns.barplot(data=bonk, x="column_count", y="accuracy_overall", ax=ax, hue='name')

        for index, row in bonk.iterrows():
            barplot.text(row.name, 0.1, row.variation, color='black', ha="left", rotation="vertical")

        self.logger.log_img(self.base_name + "acc_over_col_bar")

        fig, ax = plt.subplots(figsize=(16, 8))
        _ = sns.lineplot(data=bonk, x="column_count", y="accuracy_overall", ax=ax, hue='name')
        self.logger.log_img(self.base_name + "acc_over_col_line")

    def display_acc_config_column_heatmap(self):
        cols = ['variation', 'column_count', 'accuracy_overall']
        bap = self.frame[cols]
        fig, ax = plt.subplots(figsize=(16, 8))

        try:
            acura = bap.pivot(*cols)
            _ = sns.heatmap(acura)
            self.logger.log_img(self.base_name + "acc_over_col_heatmap")
        except Exception as e:
            self.logger.info(f"Could not create heatmap {e}")
            print(e)

    @staticmethod
    def barchart(df: pd.DataFrame, logger: Logger, x: str, y: str, name: str, hue=None):
        fig, ax = plt.subplots(figsize=(16, 8))
        plot = sns.barplot(data=df, x=x, y=y, ax=ax, hue=hue)
        for lbl in plot.get_xticklabels():
            lbl.set_rotation(90)
        # plt.xticks(rotation=70)
        logger.log_img(f"{name}")
