from typing import List, Tuple
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import time
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


CLASSIFICATION_DICT = {'technical_debt': 0, 'feature': 1,
                       'architecture': 2, 'defect': 3, 'research_spike': 4}
PRIORITY_DICT = {'': 0, '1 - Critical': 1, '2 - High': 2,
                 '3 - Moderate': 3, '4 - Low': 4, '5 - Planning': 5}
STATE_DICT = {'Draft': 0, 'Ready': 1, 'Work in progress': 2, 'Review': 3,
              'Testing': 4, 'Quality Assurance': 5, 'Deployment': 6, 'Complete': 7, 'Cancelled': 8,
              # Added not real states
              'Stale': 9,
              'Other': 10
              }
TEXT_COLUMNS = ['short_description', 'description',
                'proposed_solution', 'acceptence_crit']


def reverse_dict(d):
    return dict((v, k) for k, v in d.items())


def load_story_commit(path: str) -> pd.DataFrame:
    data = pd.read_csv(path)
    return data


def get_finished_stories(frame: pd.DataFrame) -> pd.DataFrame:
    # cancelled = str(state_dict["Cancelled"])
    completed = STATE_DICT['Complete']
    cancelled = STATE_DICT['Cancelled']

    result = frame[(frame.state == completed) | (frame.state == cancelled)]
    result = result.drop(['is_stale', 'last_update'])
    return result

def row_state_mapper(row) -> int:
    completed = STATE_DICT['Complete']
    cancelled = STATE_DICT['Cancelled']
    stale = STATE_DICT['Stale']
    other = STATE_DICT['Other']

    state = row['state']
    is_stale = row['is_stale']

    if state == completed or state == cancelled:
        return state

    if is_stale:
        return stale
    else:
        return other


def vectorize_text_field(field: str,  df: pd.DataFrame, count_vect=None) -> Tuple[pd.DataFrame, CountVectorizer]:
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
    return (vector_frame, count_vect)


def vectorize_and_join(field: str,  df: pd.DataFrame, count_vect=None, prefix_word=None) -> Tuple[pd.DataFrame, CountVectorizer]:
    (vector_frame, count_vect) = vectorize_text_field(field, df, count_vect)

    prefix_word = prefix_word if prefix_word is not None else field

    frame = pd.concat([
        df.drop(field, axis=1).reset_index(),
        vector_frame.add_prefix("__{}_".format(prefix_word))
    ], axis=1)

    return (frame, count_vect)


def get_xy_from_stories(df: pd.DataFrame, fields_to_drop=['state'], y_field='state') -> Tuple[pd.DataFrame, pd.DataFrame]:
    if y_field not in fields_to_drop:
        fields_to_drop.append(y_field)

    X = df.drop(fields_to_drop, axis=1)
    y = df[y_field]
    return (X, y)


def scale_stories(df: pd.DataFrame, scaler=None) -> pd.DataFrame:
    if scaler is None:
        scaler = MinMaxScaler()
        scaler.fit(df[df.columns])

    scaled = scaler.transform(df)
    scaled_df = pd.DataFrame(scaled, columns=df.columns)
    return scaled_df, scaler

def get_scaled_xy_from_df(stories, story_filter=get_finished_stories,  scaler=None, fields_to_drop=['state']) -> Tuple[pd.DataFrame, pd.DataFrame]:
    stories = story_filter(stories) if story_filter is not None else stories
    (X, y) = get_xy_from_stories(stories, fields_to_drop)
    (scaled_X, scaler) = scale_stories(X, scaler)
    return (scaled_X, y, stories, scaler)

def get_scaled_xy(path: str, story_filter=get_finished_stories,  scaler=None, fields_to_drop=['state']) -> Tuple[pd.DataFrame, pd.DataFrame]:
    original = load_story_commit(path)
    stories = story_filter(original) if story_filter is not None else original
    (X, y) = get_xy_from_stories(stories, fields_to_drop)
    (scaled_X, scaler) = scale_stories(X, scaler)
    return (scaled_X, y, stories, scaler)


def get_dfs_from_file(path: str, story_filter=get_finished_stories, test_size=0.20) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    # original = load_story_commit(path)
    # stories = story_filter(original) if story_filter is not None else original
    # (X, y) = get_xy_from_stories(stories)
    (X, y, original, scaler) = get_scaled_xy(path, story_filter)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size)
    return (X_train, X_test, y_train, y_test, original, scaler)


def test_svm_kernel(kernel, X_train, X_test, y_train, y_test, full_log=False):
    if (full_log):
        print('\nTesting: {}'.format(kernel))

    start = time.time()
    svclassifier = SVC(kernel=kernel, probability=True)
    svclassifier.fit(X_train, y_train)

    y_pred = svclassifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    duration = time.time() - start

    if (full_log):
        print('Testing took: {} seconds'.format(duration))
        print("Accuracy:", accuracy)
        # print(confusion_matrix(y_test,y_pred))
        # print(classification_report(y_test,y_pred))

    return (kernel, accuracy, duration)


def test_svm_kernels(X_train, X_test, y_train, y_test, full_log=False):
    kernels = ['poly', 'rbf', 'sigmoid', 'linear']
    svm_accuracy = []
    for k in kernels:
        svm_accuracy.append(test_svm_kernel(
            k, X_train, X_test, y_train, y_test, full_log))

    return pd.DataFrame(sorted(svm_accuracy, key=lambda x: x[1], reverse=True), columns=['Kernel', 'Accuracy', 'Duration'])
