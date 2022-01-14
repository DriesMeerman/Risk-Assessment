from __future__ import annotations
from enum import Enum
import pandas as pd
import seaborn as sns
import time
import matplotlib.pyplot as plt
from IPython.display import display
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import OrdinalEncoder
from sklearn import metrics

from helpers.logger import Logger
from helpers.scikit_helper import *
from helpers.util import *
from models.config_helper import *
from helpers import dataframe_column_bias_pie_chart


class DatasetType(Enum):
    TRAIN = 1
    VALIDATE = 2
    TEST = 3


class ModelTest:
    def __init__(self, training_df: pd.DataFrame, config: ConfigHelper, feature_variation: str) -> None:
        self.config = config
        self.feature_config = config.configs[feature_variation]
        self.variation = feature_variation
        self.logger = Logger(config.verbosity, config.print_markdown, config.file_name, img_format='png')
        self.input_data = training_df
        self.order_graph = False
        self.model = None
        self.X = None
        self.y = None
        self.scaler = None
        self.vectorizers = None
        self.X_train = None
        self.X_test = None
        self.X_validate = None
        self.y_train = None
        self.y_test = None
        self.y_validate = None
        self.y_pred_train = None
        self.y_pred_test = None
        self.y_pred_val = None
        self.accuracy_train = None
        self.accuracy_test = None
        self.accuracy_val = None
        self.accuracy = None
        self.acc_report_frame = None # dataframe
        self.best_mean_fit_time = None
        self.name = None
        self.name_short = None
        self.columns = None
        self.encoders = {}

        self.load_xy(training_df)
        # self.set_train_val_test()

    def get_description(self):
        return f"{self.variation}_{self.name}"

    def vectorize_text(self, frame: pd.DataFrame) -> pd.DataFrame:
        if 'vectorize_fields' not in self.feature_config or not self.feature_config['vectorize_fields']:
            self.vectorizers = {}
            return frame

        fields = self.feature_config['vectorize_fields']
        vectorizers = {}
        new_frame = frame
        for field in fields:
            self.logger.debug("Vectorizing {}".format(field))
            vecto = self.vectorizers[field] if self.vectorizers is not None and field in self.vectorizers else None
            new_frame, count_vect = vectorize_and_join(field, new_frame, count_vect=vecto)
            vectorizers[field] = count_vect

        self.vectorizers = vectorizers
        return new_frame

    def ordinal_encode(self, frame, columns):
        frame = frame.copy()
        for col in columns:
            if col not in frame:
                print(f"Warn trying to ordinally encode {col} from config but it is not part of frame")
                return frame

            X = frame[[col]]
            if col not in self.encoders:
                enc = OrdinalEncoder()
                enc.fit(X)
                self.encoders[col] = enc
            else:
                enc = self.encoders[col]
            frame[col] = enc.transform(X)
        return frame

    def load_xy(self, input_frame):
        vector_fields = self.feature_config["vectorize_fields"]

        if self.config.zeroshot_configs is not None and len(self.config.zeroshot_configs) > 0:
            ml_pre_process_fields = list(self.config.zeroshot_configs.keys())

            if self.config.sentiment_analysis:
                ml_pre_process_fields.append("_sentiment")

            input_frame = self.ordinal_encode(input_frame, ml_pre_process_fields)

        y_frame = input_frame[self.config.y_column]
        if self.config.scale_full_set:
            frame = input_frame[self.feature_config["x_cols"] + vector_fields]
            vectorized_frame = self.vectorize_text(frame)
            scaler = MinMaxScaler()
            scaled_x = scaler.fit_transform(vectorized_frame)

            self.columns = vectorized_frame.columns
            self.X = scaled_x
            self.scaler = scaler
        else:
            # When this flow?
            if "zeroshot_fields" in self.feature_config:
                col = self.feature_config["zeroshot_fields"][0]
                if col in input_frame.columns:
                    self.X = input_frame[self.feature_config["x_cols"] + vector_fields]
                else:
                    basic_x_cols = set(self.feature_config["x_cols"]) - set(self.feature_config["zeroshot_fields"])
                    self.X = input_frame[list(basic_x_cols) + vector_fields]
            else:
                self.X = input_frame[self.feature_config["x_cols"] + vector_fields]

        self.y = y_frame
        self.set_train_val_test()

    """
    Example math split
    # 0.85
    # 0.15 / 0.85 = 0,1764705882
    # 0.85 * 0.176 ~= 0.15
    """
    def set_train_val_test(self):
        test_size = self.config.test_size
        validation_size = self.config.validation_size
        rest_size = 1 - validation_size

        random_state = self.config.random_seed
        test_from_train = validation_size / rest_size
        self.logger.info("Using seed for random split {}".format(random_state))
        self.logger.debug(
            "SIZES:   \n\ttrain {}  \n\ttest {}  \n\tvalidate {}  \n".format(1 - (test_size + validation_size), test_size,
                                                                     validation_size))

        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=validation_size,
                                                            random_state=random_state)
        X_train, X_validate, y_train, y_validate = train_test_split(X_train, y_train, test_size=test_from_train,
                                                                    random_state=random_state)
        self.logger.debug("Data shape\n\tTraining rows:\t{}  \n\tcolumns:\t{}  \n".format(*X_train.shape))

        if not self.config.scale_full_set:
            vectorized_frame_x_train = self.vectorize_text(X_train)
            vectorized_frame_x_test = self.vectorize_text(X_test)
            vectorized_frame_x_validate = self.vectorize_text(X_validate)
            scaler = MinMaxScaler()
            X_train = scaler.fit_transform(vectorized_frame_x_train)
            X_test = scaler.fit_transform(vectorized_frame_x_test)
            X_validate = scaler.fit_transform(vectorized_frame_x_validate)

            self.columns = vectorized_frame_x_train.columns
            # self.X = scaled_x

        self.X_train = X_train
        self.X_test = X_test
        self.X_validate = X_validate
        self.y_train = y_train
        self.y_test = y_test
        self.y_validate = y_validate

    def get_train_data_shape(self):
        return self.X_train.shape

    def plot_state_y_distribution(self, set: pd.DataFrame, set_type: DatasetType):
        dataframe_column_bias_pie_chart(set, self.config.y_column, self.config.y_column, self.config.y_labels)
        self.logger.log_img(f"classification_output_distribution_with_{set_type.name}")

    def plot_output_distribution_for_set(self, set_type: DatasetType):
        df = pd.DataFrame()

        if set_type == DatasetType.TEST:
            df[self.config.y_column] = self.y_test
        elif set_type == DatasetType.TRAIN:
            df[self.config.y_column] = self.y_train
        elif set_type == DatasetType.VALIDATE:
            df[self.config.y_column] = self.y_validate

        count = len(df.index)
        self.logger.info("Distribution for: {}, {} with a rowcount of {}".format(set_type.name, self.config.y_column, count))
        return self.plot_state_y_distribution(df, set_type)

    def set_training_data(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=self.config.test_size)
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def train_model(self):
        raise NotImplementedError(self.__class__.__name__ + '.train_model')

    def calc_accuracy(self):
        model = self.model

        start = time.time()
        self.logger.debug("Start prediction")
        self.y_pred_train = model.predict(self.X_train)
        self.y_pred_test = model.predict(self.X_test)
        self.y_pred_val = model.predict(self.X_validate)
        self.logger.debug("Finished prediction in {}".format(round(time.time() - start, 2)))
        self.accuracy_train = accuracy_score(self.y_train, self.y_pred_train)
        self.accuracy_test = accuracy_score(self.y_test, self.y_pred_test)
        self.accuracy_val = accuracy_score(self.y_validate, self.y_pred_val)
        self.accuracy = ((self.accuracy_test + self.accuracy_val) / 2)
        f_report = metrics.classification_report(self.y_train, self.y_pred_train, output_dict=True)
        self.acc_report_frame = pd.DataFrame(f_report).transpose()
        self.logger.csv(self.acc_report_frame, f"{self.variation}_{self.name}_{self.accuracy}.csv", "acc_report/")
        self.logger.debug(
            "\nAccuracy train set = \t\t{}" +
            "\nAccuracy test set = \t\t{}" +
            "\nAccuracy validation set = \t{}" +
            "\nAverage Accuracy = \t\t{}\n".format(
                self.accuracy_train, self.accuracy_test, self.accuracy_val, self.accuracy))

    @staticmethod
    def get_model(frame: pd.DataFrame, config: ConfigHelper, variation: str) -> ModelTest:
        raise NotImplementedError('.get_model')

    def optimize_config(self):
        raise NotImplementedError(self.__class__.__name__ + '.optimize_config')

    def optimize_config_stub(self, parameter_space, model):
        cpu_count = self.config.cpu_count
        self.logger.debug("Using Gridsearch to find optimal model, using {} cores".format(cpu_count))
        start = time.time()
        searcher = GridSearchCV(model, parameter_space, cv=3, n_jobs=cpu_count, verbose=3)
        searcher.fit(self.X_train, self.y_train)

        self.logger.debug("Grid search to find best params took {} seconds".format(round(time.time() - start, 2)))
        self.model = searcher.best_estimator_
        self.logger.debug("Fitted using gridsearch")
        self.logger.info('Best parameters found:\n', searcher.best_params_, '\n')
        self.best_mean_fit_time = searcher.cv_results_['mean_score_time'][searcher.best_index_]
        self.calc_accuracy()
        self.display_accuracy(searcher.cv_results_, parameter_space)

    def display_accuracy(self, cv_results: pd.DataFrame, hyper_params: Dict):
        means = cv_results['mean_test_score']
        stds = cv_results['std_test_score']
        fit_time = cv_results['mean_fit_time']
        results = pd.concat(
            [pd.DataFrame({'mean': means, 'std': stds, 'time': fit_time}), pd.DataFrame(cv_results['params'])], axis=1)

        accuracy_frame = results.copy()
        frame_length = len(accuracy_frame.index)
        ordered = accuracy_frame.sort_values(by=['mean'], ascending=False)
        half_table_size = 6
        front = ordered.head(half_table_size)
        tail_grab = half_table_size if (frame_length - half_table_size) > half_table_size else (
                    frame_length - half_table_size)
        end = None if frame_length < half_table_size else ordered.tail(tail_grab)
        self.logger.info("Showing {} best and {} worst results".format(half_table_size, half_table_size))
        if end is not None:
            self.logger.df(pd.concat([front, end]))
            # display(pd.concat([front, end]))
        else:
            self.logger.df(front)
            # display(front)

        for key in hyper_params.keys():
            accuracy_frame[key] = accuracy_frame[key].map(str)

        accuracy_frame['time'] = accuracy_frame['time'].map(lambda n: round(n, 3))
        accuracy_frame['Name'] = accuracy_frame[hyper_params.keys()].agg('-'.join, axis=1)

        sort_graph = self.order_graph
        max_graph_size = 30
        if frame_length > max_graph_size:
            self.logger.info(
                "Force ordering of graph due to size, limiting output to {} best performers".format(max_graph_size))
            sort_graph = True

        visual = accuracy_frame[['Name', 'mean', 'time']] if not sort_graph else accuracy_frame[
            ['Name', 'mean', 'time']].sort_values(by=['mean'], ascending=False)
        visual.columns = ['Name', 'Accuracy', 'Time']
        cm = sns.light_palette("green", as_cmap=True)
        accuracy_frame.style.background_gradient(cmap=cm)
        fig, ax = plt.subplots(figsize=(8, 8))
        sns.set(style="whitegrid")
        sns.barplot(y='Name', x="Accuracy", data=visual.head(max_graph_size), ax=ax)

        self.save_plot()

    def save_plot(self):
        seconds = round(round(time.time()))
        filename = f"{self.name_short}_{self.variation}_{seconds}"
        self.logger.log_img(filename)
        # save_fig(filename, None, self.logger)

    def get_total_row_count(self):
        return len(self.X)
        # return len(self.X.index)

    def get_train_row_count(self):
        return len(self.X_train)

    def __str__(self) -> str:
        output = "Model: {}"
        output += "Accuracy: {}"
        output += "TotalRowCount: {}"

        output = output.format(self.name,
                               self.accuracy,
                               self.get_total_row_count()
                               )
        return output
