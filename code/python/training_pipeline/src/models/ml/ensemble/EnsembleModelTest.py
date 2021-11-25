from abc import ABC

import pandas as pd

from models.ml.ModelTest import ModelTest


class EnsembleModelTest(ModelTest, ABC):
    def __init__(self, training_df: pd.DataFrame, config, feature_variation: str) -> None:
        super().__init__(training_df, config, feature_variation)
