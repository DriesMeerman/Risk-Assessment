import math
from typing import Dict
import pandas as pd

from models.ml.ensemble.EnsembleModelTest import *
from sklearn.ensemble import RandomForestClassifier


class RandomForrestModelTest(EnsembleModelTest):

    def __init__(self, training_df: pd.DataFrame, config, feature_variation: str) -> None:
        super().__init__(training_df, config, feature_variation)
        self.name = 'RandomForrest'
        self.name_short = 'RF'

    def train_model(self):
        pass

    @staticmethod
    def get_model(frame: pd.DataFrame, config, variation: str) -> ModelTest:
        return RandomForrestModelTest(frame, config, variation)

    def optimize_config(self):
        row_count = self.get_train_row_count()

        depths = {
            'All':  None,
            'Log':  round(math.log(row_count)),
            'Sqrt': round(math.sqrt(row_count)),
            '75%':  round(row_count * 0.75),
            '50%':  round(row_count / 2),
            '25%':  round(row_count / 4),
            '5': 5
        }

        hyper_parameters = {
            'n_estimators': [50, 100],
            'criterion': ['gini', 'entropy'],
            'max_features': ['auto', 'sqrt', 'log2'],
            'class_weight': ['balanced', 'balanced_subsample', None],
            'max_depth': list(depths.values())
        }
        self.optimize_config_stub(hyper_parameters, RandomForestClassifier())
