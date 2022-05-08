from typing import List
import time
import pandas as pd
import json

from .util import pickle_make, path_helper


class ModelContainer:
    def __init__(self, name, description, model, columns, scaler, vectorizers, config, variation, accuracy,
                 accuracy_train, accuracy_test, accuracy_val, best_mean_fit_time,
                 standardizer, topic_analysers, ordinal_encoder):
        self.name = name
        self.description = description
        self.ml_model = model
        self.scaler = scaler
        self.vectorizers = vectorizers
        self.config = config
        self.variation = variation
        self.configured_columns = config.get_variation_columns(variation)
        self.columns = columns
        self.accuracy = accuracy
        self.accuracy_train = accuracy_train
        self.accuracy_test = accuracy_test
        self.accuracy_val = accuracy_val
        self.best_mean_fit_time = best_mean_fit_time
        self.standardizer = standardizer
        self.topic_analyser = topic_analysers
        self.ordinal_encoder = ordinal_encoder

    def get_col_count(self):
        if self.columns is not None:
            return len(self.columns)

        return len(self.config.dataframe.columns)

    def save(self):
        epoch_hours = int(time.time() / 3600)
        base_folder = f"/containers/{self.accuracy}_{self.description}_[{epoch_hours}]/"
        folder = self.config.output_folder + base_folder
        print(f"Saving to: {base_folder}")

        pickle_wrap = lambda file, data: pickle_make(file, data, folder_override=folder)
        # Code to save each individual thing T_T, because the whole thing cannot be re-opened

        self.save_metadata("meta.json", folder)
        pickle_wrap("ml_model", self.ml_model)
        pickle_wrap("ordinal_encoder", self.ordinal_encoder)
        pickle_wrap("scaler", self.scaler)
        pickle_wrap("standardizer", self.standardizer)
        pickle_wrap("topic_analyzer", self.topic_analyser)
        pickle_wrap("vectorizers", self.vectorizers)

    def save_metadata(self, name, folder):
        data = {
            "name": self.name,
            "description": self.description,
            "variation": self.variation,
            "accuracy": {
                "overall": self.accuracy,
                "train": self.accuracy_train,
                "test": self.accuracy_test,
                "validation": self.accuracy_val
            },
            "best_mean_fit_time": self.best_mean_fit_time,
            "input_columns": self.configured_columns,
            "columns": self.columns.values.tolist(),
            "config": self.config.raw
        }

        # data_string = json.dumps(data) # string vs directly to a file
        file_path = path_helper(name, folder_override=folder)
        with open(file_path, 'w') as file:
            json.dump(data, file)

    def __str__(self):
        return f"{self.name}\n{self.ml_model}\n{self.scaler}\n{self.columns}\n{self.vectorizers}\n{self.config}"


def container_list_to_df(containers: List[ModelContainer]):
    df = pd.DataFrame(columns=["name", "variation", "accuracy_overall", "accuracy_train",
                               "accuracy_test", "accuracy_val", "fit_time", "model_config"])
    for c in containers:
        row = {
            "name": c.name,
            "variation": c.variation,
            "accuracy_overall": c.accuracy,
            "accuracy_train": c.accuracy_train,
            "accuracy_test": c.accuracy_test,
            "accuracy_val": c.accuracy_val,
            "fit_time": c.best_mean_fit_time,
            "column_count": c.get_col_count(),
            "model_config": str(c.ml_model)
        }
        df = df.append(row, ignore_index=True)

    return df
