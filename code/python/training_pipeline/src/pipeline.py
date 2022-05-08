import sys
import time
from typing import List

import yaml
import arrow
import pandas as pd
import matplotlib.pyplot as plt

from helpers import Logger, Verbosity
from models import config_helper, NBModelTest, DatasetType, ExecutionType, ConfigHelper
from helpers import container_list_to_df

from services import compare_models, display_model_comparison, VariationVisualizer, ModelTest, DimensionReductionService
from services.compare_service import ALL_ENSEMBLE_MODELS, FAST_SINGLE_MODELS, ALL_SINGLE_MODELS, FAST_ENSEMBLE_MODELS
from helpers.vector_helper import vectorize_text


def parse_args():
    if len(sys.argv) < 2:
        print("No config file passed stopping")
        sys.exit(1)

    config_path = sys.argv[1]
    debug = True if len(sys.argv) > 2 and sys.argv[2] == "debug" else False

    return config_path, debug


def initialize_config(config_path: str, current_time: arrow, debug=False):
    try:
        config = config_helper.config_from_file(config_path)
    except yaml.YAMLError as exc:
        print("Error in yaml", exc)
        sys.exit(1)

    current_text = current_time.format('YYYY-MM-DD HH_mm_ss')
    if config.output_folder_postfix is not None:
        folder_name = current_text + "_" + config.output_folder_postfix
    else:
        folder_name = current_text

    if debug:
        folder_name = folder_name + "_debug"

    Logger.current_run = folder_name + "/"
    config.output_folder = "output/" + folder_name

    print("USING:\n")
    config.pretty_print()
    print("\n\n\n")
    return config


def model_optimize_compare(config, logger: Logger, start_time: arrow, models: List[ModelTest], debug: bool):
    variation_containers = pd.DataFrame()
    best_variations = pd.DataFrame()
    configs_texts = []
    variation_timings = []

    logger.info("# Comparing variations")
    feature_variations = list(config.get_variation_names())
    # models = ALL_MODELS

    if debug:
        print("debug yes")
        logger.debug("Debugging mode going faster")
        feature_variations = feature_variations[:2]

    for variation in feature_variations:
        variation_start = time.time()
        logger.info(f"Validating feature set {variation}")
        df, model_containers, best_model_container = compare_models(config, variation, models, logger)
        if best_model_container is not None:
            configs_texts.append(
                [(variation, best_model_container.accuracy, best_model_container.name, best_model_container.ml_model)]
            )
        else:
            logger.warning("No best model for variation")

        if config.save_all:
            print("saving all")
            for container in model_containers:
                container.save()

        models_df = container_list_to_df(model_containers)
        variation_containers = variation_containers.append(models_df, ignore_index=True)
        best_variations = best_variations.append(container_list_to_df([best_model_container]), ignore_index=True)

        if config.save_best and not config.save_all:
            print("saving best")
            best_model_container.save()

        logger.info(f"\n\n### model comparisons for {variation}")
        logger.df(models_df)
        display_model_comparison(models_df, variation, logger)
        logger.info("\n\n")

        variation_end = time.time()
        timing_dict = {
            "variation": variation,
            "start": variation_start,
            "end": variation_end,
            "duration": variation_end - variation_start
        }

        variation_timings.append(timing_dict)

        logger.info("\n\n", df.to_markdown(), "\n\n")
        logger.info(
            "Best in set was {} with an accuracy {}".format(best_model_container.name, best_model_container.accuracy))
        logger.info(f"\n==  {variation} == \n================================  \n\n")

    # parse column count to ints
    best_variations["column_count"] = best_variations["column_count"].astype(int)
    variation_containers["column_count"] = variation_containers["column_count"].astype(int)

    logger.info("# Configs")
    logger.list(configs_texts)

    logger.info("# RESULTS:")
    all_variations_scatterplot(variation_containers, logger)
    display_variations_log(variation_containers, logger, "all", True)
    display_variations_log(best_variations.sort_values(by=['accuracy_overall'], ascending=False), logger, "best")

    all_no_dt = variation_containers[variation_containers.name != "Decision Tree"]
    best_no_dt = all_no_dt.sort_values(by=['accuracy_overall'], ascending=False)

    best_no_dt = best_no_dt.groupby('variation', as_index=False).first()
    # as_index (default True) removes the variation key from the resulting frame cuasing errors down the line

    if len(best_no_dt.index) != 0:
        display_variations_log(best_no_dt, logger, "best_no_dt", True)
    else:
        logger.info("## Best no DT \n Best only had DT Nothing to show here")

    try:
        logger.info("# Data distribution")
        cols = config.dataframe.columns
        if 'Index' in cols:
            cols.remove('Index')

        variation_names = list(config.get_variation_names())
        variation = variation_names[0]

        config.configs[variation]['x_cols'] = config.dataframe.select_dtypes(include=['float64', 'int64']) # config.configs[variation]['x_cols'][:1]
        some_model = NBModelTest.get_model(config.dataframe, config, variation)
        for t in DatasetType:
            some_model.plot_output_distribution_for_set(t)
    except:
        print("Something went wrong while printing data distribution")
        logger.warning("Something went wrong while printing data distribution")

    finish_time = arrow.utcnow()
    logger.info("# duration\nTimes are described in utc.\n")
    logger.info(f"Started {start_time.format('YYYY-MM-DD HH:mm:ss')}")
    logger.info(f"Finished {finish_time.format('YYYY-MM-DD HH:mm:ss')}")
    total_duration = finish_time - start_time
    logger.info(f"Duration: {str(total_duration)}")

    logger.info("## Detailed duration")
    duration_df = pd.DataFrame(variation_timings)
    # visual = VariationVisualizer(None, logger, "overall_timing_")
    VariationVisualizer.barchart(duration_df, logger, x="variation", y="duration", name="overall_variation_timings")

def all_variations_scatterplot(df: pd.DataFrame, logger: Logger):
    vapor_colors = ['#01cdfe', '#05ffa1', '#b967ff', '#fffb96', '#ff71ce']
    color_palette = vapor_colors + ['#004c4c', '#001eff']  # 7 models so need 2 more colors

    color_map = {
        'k-Nearest Neighbour': '#01cdfe',
        'Guassian Naive Bayes': '#05ffa1',
        'Multinominal Naive Bayes': '#b967ff',
        'Decision Tree': '#fffb96',
        'Support Vector Machine (classifier)': '#ff71ce',
        'Stochastic Gradient Descent': '#004c4c',
        'Multi-layer Perceptron': '#001eff',
        # ensemble colors
        'AdaBoost': '#01cdfe',
        'Bagging': '#05ffa1',
        'Stacking': '#b967ff',
        'RandomForrest': '#ff71ce',
        'GradientBoost': '#001eff'
    }
    figsize = (14, 8)
    fig, ax = plt.subplots()
    grouped = df.groupby('name')
    for key, group in grouped:
        group.plot(ax=ax, kind='scatter', x='variation', y='accuracy_overall', label=key, color=color_map[key], rot=90,
                   figsize=figsize)

    logger.log_img("variation_model_performance")


def display_variations_log(variations, logger, name: str, save_graphs=False):
    logger.info(f"## {name}")
    logger.df(variations.sort_values(by=['accuracy_overall'], ascending=False))
    logger.csv(variations, f"{name}_variations.csv")

    if save_graphs:
        visual = VariationVisualizer(variations, logger, base_name=f"overall_{name}_")
        visual.display_accuracy_over_variation()
        visual.display_acc_over_time()
        visual.display_acc_over_col_per_variation()
        visual.display_acc_config_column_heatmap()
        return visual


def input_analysis(config: ConfigHelper, logger: Logger):
    dimensionService = DimensionReductionService(logger)
    logger.info(f"# Data balance / bias comparison")
    for name, feature_config in config.configs.items():
        logger.info(f"## {name}")
        columns = config.get_variation_columns(name)
        vect_columns = config.get_vector_columns(name)
        x_frame = config.dataframe[columns + vect_columns]
        vect_frame, _ = vectorize_text(x_frame, logger, vect_columns)
        dimensionService.compare_reducers(vect_frame, config.dataframe[[config.y_column]], config.y_column, name)


def main():
    start_time = arrow.utcnow()
    config_path, debug = parse_args()
    config = initialize_config(config_path, start_time, debug)

    # Load dataset
    count = 200 if debug else None
    config.load_data(count)

    # setup logger
    logger = Logger(config.verbosity, config.print_markdown, config.file_name, img_format='png')

    models = None
    if config.type == ExecutionType.single:
        models = ALL_SINGLE_MODELS

        if debug:
            models = FAST_SINGLE_MODELS
    else:
        models = ALL_ENSEMBLE_MODELS
        # if debug:
        #     models = FAST_ENSEMBLE_MODELS

    if not debug and not config.skip_dim_reduction:
        input_analysis(config, logger)


    # Run comparison
    model_optimize_compare(config, logger, start_time, models, debug)


if __name__ == "__main__":
    main()
