from typing import Dict, Tuple
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd
import numpy as np


def vectorize_text_field(field: str, df: pd.DataFrame, count_vect=None) -> Tuple[pd.DataFrame, CountVectorizer]:
    word_frame = df[field].replace(np.nan, '', regex=True)

    if not count_vect:
        count_vect = CountVectorizer(analyzer='word',
                                     token_pattern='[a-zA-Z0-9]{3,}',
                                     stop_words='english')
        count_vect.fit(word_frame)

    word_vecs = count_vect.transform(word_frame)

    # word_vecs = count_vect.fit_transform(word_frame)
    vector_frame = pd.DataFrame(
        word_vecs.toarray(), columns=count_vect.get_feature_names())
    return vector_frame, count_vect


def vectorize_and_join(field: str, df: pd.DataFrame, count_vect=None, prefix_word=None) -> Tuple[
    pd.DataFrame, CountVectorizer]:
    vector_frame, count_vect = vectorize_text_field(field, df, count_vect)

    prefix_word = prefix_word if prefix_word is not None else field

    frame = pd.concat([
        df.drop(field, axis=1).reset_index(),
        vector_frame.add_prefix("__{}_".format(prefix_word))
    ], axis=1)

    return frame, count_vect


def vectorize_text(frame: pd.DataFrame, logger, fields=None) -> Tuple[pd.DataFrame, Dict]:
    if fields is None:
        return frame, {}

    vectorizers = {}
    new_frame = frame
    for field in fields:
        logger.debug("Vectorizing {}".format(field))
        new_frame, count_vect = vectorize_and_join(field, new_frame)
        vectorizers[field] = count_vect

    return new_frame, vectorizers
