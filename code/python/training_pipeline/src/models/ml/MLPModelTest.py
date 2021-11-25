import time
from typing import Dict
import pandas as pd
from sklearn.neural_network import MLPClassifier

from .ModelTest import ModelTest, ConfigHelper


class MLPModelTest(ModelTest):
    def __init__(self, training_df: pd.DataFrame, config, variation: str) -> None:
        super().__init__(training_df, config=config, feature_variation=variation)
        self.name = "Multi-layer Perceptron"
        self.name_short = "MLP"
        self.solver = 'adam'  # 'lbfgs'
        self.random_state = self.config.random_seed
        self.hidden_layer = (100, 100)
        self.alpha = 1e-5
        self.max_iterations = self.get_total_row_count()

    def train_model(self):
        self.logger.debug("Start training.")
        start = time.time()

        model = MLPClassifier(solver=self.solver,
                              alpha=self.alpha,
                              hidden_layer_sizes=self.hidden_layer,
                              random_state=self.random_state,
                              max_iter=self.max_iterations
                              )
        model.fit(self.X_train, self.y_train)
        fit_time = round(time.time() - start, 2)
        self.logger.debug("Fit model in {} seconds".format(fit_time))
        self.model = model
        self.calc_accuracy()
        self.fit_time = fit_time

    def optimize_config(self):
        # self.train_model()
        # https://datascience.stackexchange.com/questions/36049/how-to-adjust-the-hyperparameters-of-mlp-classifier-to-get-more-perfect-performa
        parameter_space = {
            # 'hidden_layer_sizes': [(50), (50,50), (100, 50), (100,100), (200, 50), (200, 100)], % takes too much time
            'activation': ['tanh', 'relu'],
            'solver': ['sgd', 'adam', 'lbfgs'],
            'alpha': [0.0001, 0.05],
            'learning_rate': ['constant', 'adaptive'],
        }

        self.optimize_config_stub(parameter_space, MLPClassifier(max_iter=1000))

    @staticmethod
    def get_model(frame: pd.DataFrame, config: ConfigHelper, variation: str):
        return MLPModelTest(frame, config, variation)
