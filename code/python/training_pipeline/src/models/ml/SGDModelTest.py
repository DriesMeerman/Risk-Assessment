from typing import Dict
import pandas as pd
from sklearn.linear_model import SGDClassifier

from .ModelTest import ModelTest, ConfigHelper


class SGDModelTest(ModelTest):
    def __init__(self, training_df: pd.DataFrame, config: ConfigHelper, variation: str) -> None:
        super().__init__(training_df, config, variation)
        self.name = "Stochastic Gradient Descent"
        self.name_short = "SGD"

    def train_model(self):
        self.logger.warning("Lol nope")

    def optimize_config(self):
        parameter_space = {
            'loss': ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron', 'squared_loss', 'huber'],
            # , 'epsilon_insensitive', 'squared_epsilon_insensitive'],
            'penalty': ['l2', 'l1', 'elasticnet'],
            'alpha': [0.00001, 0.05],
            'learning_rate': ['constant', 'optimal', 'invscaling', 'adaptive']
        }

        self.optimize_config_stub(parameter_space, SGDClassifier(max_iter=1000, eta0=100.0))

    @staticmethod
    def get_model(frame: pd.DataFrame, config: ConfigHelper, variation: str):
        return SGDModelTest(frame, config, variation)
