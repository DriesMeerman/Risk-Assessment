from enum import Enum
from typing import Dict

import pprint
import pandas as pd
from pathlib import Path
import sys

from helpers.util import *


class ExecutionType(Enum):
    single = 1
    ensemble = 2


def determine_type(exec_type):
    if exec_type == "single" or exec_type == 1:
        return ExecutionType.single
    if exec_type == "ensemble" or exec_type == 2:
        return ExecutionType.ensemble


class ZeroShotConfig:
    def __init__(self, name: str, labels):
        self.name = name
        self.labels = labels

    def __str__(self):
        return f"{self.name} : {str(self.labels)}"


class ConfigHelper:
    def __init__(self, data, load_frame=False) -> None:
        self.variables = data["variables"]
        self.verbosity = data["verbosity"]
        self.print_markdown = data["print_markdown"] if "print_markdown" in data else True
        self.file_name = data["log_file_name"] if "log_file_name" in data else None
        self.type = determine_type(data["type"]) if "type" in data else ExecutionType.single
        self.random_seed = data["random_seed"]
        self.cpu_count = data["cpu_corecount"]
        self.training_path = data["training_path"]
        self.y_column = data["y_column"]
        self.y_labels = data["y_labels"] if "y_labels" in data else None
        self.save_best = data["save_best"] if "save_best" in data else False
        self.save_all = data["save_all"] if "save_all" in data else False
        self.output_folder_postfix = data["output_folder_postfix"] if "output_folder_postfix" in data else None
        self.skip_dim_reduction = data["skip_dim_reduction"] if "skip_dim_reduction" in data else True
        self.sample_count = data["sample_count"] if "sample_count" in data else None

        self.train_size = data["train_size"]
        self.test_size = data["test_size"]
        self.validation_size = data["validation_size"]
        # Scaling full set means scaling happens before splitting data which is bas this should be removed from config
        self.scale_full_set = data["scale_full_set"] if "scale_full_set" in data else False

        self.standardize_text = data["standardize_text"] if "standardize_text" in data else True
        self.lda_topic_generation = data["lda_topic_generation"] if "lda_topic_generation" in data else True

        if "ml_pre_processing" in data:
            pre_processing = data["ml_pre_processing"]
            self.sentiment_analysis = pre_processing[
                "sentiment_analysis"] if "sentiment_analysis" in pre_processing else True
            self.zeroshot_configs = self.get_zeroshot_configs(pre_processing["zeroshot_analysis"])
        else:
            self.sentiment_analysis = None
            self.zeroshot_configs = None

        self.configs = self.generate_feature_configs(data["feature_variations"], data)
        self.dataframe = None
        self.output_folder = "output/"

        if load_frame:
            self.load_data()

    def get_zeroshot_configs(self, ml_pre_processing):
        print(ml_pre_processing)
        configs = {}
        for item in ml_pre_processing:
            name = "_" + item['name']
            configs[name] = ZeroShotConfig(name, item['labels'])
        return configs

    def generate_feature_configs(self, feature_variations: Dict, raw_conf):
        result = {}
        for key, conf in feature_variations.items():
            variation = {"NAME": key}
            cols = []

            if "x_cols" in conf:
                cols = cols + conf["x_cols"]

            if "x_cols_vars" in conf:
                vars_to_use = conf["x_cols_vars"]

            cols = cols + flatten_list([self.variables[v] for v in vars_to_use])

            if "extraction_fields" in conf and self.zeroshot_configs is not None:
                zeroshot_fields = list(self.zeroshot_configs.keys())
                cols = cols + zeroshot_fields
                variation["zeroshot_fields"] = zeroshot_fields

            variation["x_cols"] = list(set(cols))
            variation["vectorize_fields"] = conf["vectorize_fields"] if "vectorize_fields" in conf else []
            variation["extraction_fields"] = conf["extraction_fields"] if "extraction_fields" in conf else []
            variation["ml_cached"] = conf["ml_cached"] if "ml_cached" in conf else False
            result[key] = variation

        return result

    def get_variation_names(self):
        return self.configs.keys()

    def get_variation_columns(self, variation: str):
        return self.configs[variation]["x_cols"]

    def get_vector_columns(self, variation: str):
        if "vectorize_fields" in self.configs[variation]:
            return self.configs[variation]["vectorize_fields"]

        return []

    def get_ml_preprocess_columns(self, variation: str):
        if "extraction_fields" in self.configs[variation]:
            return self.configs[variation]["extraction_fields"]

        return []

    def get_all_columns(self, variation):
        return self.get_variation_columns(variation) + self.get_vector_columns(variation)

    def load_data(self, row_count=None):
        file_path = Path(self.training_path).resolve()
        self.dataframe = pd.read_csv(file_path)#, keep_default_na=False)

        if self.sample_count is not None:
            self.dataframe = self.dataframe.sample(self.sample_count, random_state=42)

        if row_count is not None:
            self.dataframe = self.dataframe.sample(row_count, random_state=42)  # self.dataframe.iloc[:row_count]

    def __str__(self) -> str:
        return str(self.__dict__())

    def __dict__(self):
        return {
            "variables": self.variables,
            "verbosity": self.verbosity,
            "random_seed": self.random_seed,
            "cpu_count": self.cpu_count,
            "training_path": self.training_path,
            "y_column": self.y_column
        }

    def pretty_print(self):
        pprint.pprint(self.__dict__())


def config_from_file(path: str):
    config = load_yaml(path)
    return ConfigHelper(config)
