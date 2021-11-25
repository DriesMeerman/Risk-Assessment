import math
from typing import Dict
import pandas as pd
from sklearn.ensemble import StackingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from models.ml.ensemble.EnsembleModelTest import *


class StackingModelTest(EnsembleModelTest):
    def __init__(self, training_df: pd.DataFrame, config, feature_variation: str) -> None:
        super().__init__(training_df, config, feature_variation)
        self.name = "Stacking"
        self.name_short = "STK"

    def train_model(self):
        pass

    def optimize_config(self):
        hyper_parameters = {
            # 'stack_method': ['auto', 'predict_proba', 'decision_function', 'predict'] # auto tries the others
            'passthrough': [True, False]

        }
        estimators = [('DT', DecisionTreeClassifier()), ('KNN', KNeighborsClassifier()), ('SVC', SVC(probability=True))]
        self.optimize_config_stub(hyper_parameters, StackingClassifier(estimators))

    @staticmethod
    def get_model(frame: pd.DataFrame, config, variation: str) -> ModelTest:
        return StackingModelTest(frame, config, variation)