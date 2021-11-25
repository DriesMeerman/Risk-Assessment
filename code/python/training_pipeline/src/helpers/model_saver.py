from typing import List
import time
import pandas as pd

from .util import pickle_make


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
        epoch_hours = time.time() / 3600
        path = f"{self.description}_model_container_{epoch_hours}"
        print(f"Saving to: {path}")
        pickle_make(path, self, folder_override=self.config.output_folder + "/containers/")

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
