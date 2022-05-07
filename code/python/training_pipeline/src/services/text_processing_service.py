from enum import Enum

import pandas as pd
import numpy as np
from transformers import pipeline
import torch
import math

from sklearn.decomposition import LatentDirichletAllocation, TruncatedSVD
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV

import nltk

from models import ConfigHelper

# Initially taken from the worcloud package, partially modified
# TODO: look at https://smltar.com/stopwords.html
STOPWORDS = ['a', 'about', 'above', 'after', 'again', 'all', 'also', 'am', 'an', 'and', 'any', 'are', "aren't", 'as',
             'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', "can't",
             'cannot', 'com', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down',
             'during', 'each', 'else', 'ever', 'few', 'for', 'from', 'further', 'get', 'had', "hadn't", 'has', "hasn't",
             'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'hence', 'her', 'here', "here's", 'hers',
             'herself', 'him', 'himself', 'his', 'how', "how's", 'however', 'http', 'i', "i'd", "i'll", "i'm", "i've",
             'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', 'just', 'k', "let's", 'like', 'me',
             'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or',
             'other', 'otherwise', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'r', 'same', 'shall',
             "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'since', 'so', 'some', 'such', 'than',
             'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'therefore',
             'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too',
             'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were',
             "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's",
             'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'www', 'you', "you'd", "you'll", "you're",
             "you've", 'your', 'yours', 'yourself', 'yourselves']


class CLASSIFICATION_TASKS(Enum):
    ZERO_SHOT = "zero-shot-classification"
    SENTIMENT_ANALYSIS = "sentiment-analysis"


class CLASSIFICATION_MODELS(Enum):
    BART_LARGE = "facebook/bart-large-mnli"


class TextStandardizer:
    def __init__(self):
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')

        self.stemmer = nltk.stem.PorterStemmer()
        self.stopwords = STOPWORDS

    """
    Turns text into lowercase, removes stopwords and creates stopword count 
    then stems the sentence into a simplified form 
    """
    def standardize(self, text: str):
        if isinstance(text, float) and math.isnan(text):
            return "", 0

        simple = text.lower()
        simple, stopword_count = self.stopword_analysis(simple)
        simple = self.stem_text(simple)
        return simple, stopword_count

    def stopword_analysis(self, text: str):
        stopword_count = 0
        # https://stackabuse.com/removing-stop-words-from-strings-in-python/
        text_tokens = nltk.tokenize.word_tokenize(text)
        tokens_without_sw = [word for word in text_tokens if not word in self.stopwords]
        stopword_count = len(text_tokens) - len(tokens_without_sw)
        text = " ".join(tokens_without_sw)

        return text, stopword_count

    def stem_sentence(self, sentence, stemmer) -> str:
        token_words = nltk.tokenize.word_tokenize(sentence)
        stem_sentence = []
        for word in token_words:
            stem_sentence.append(stemmer.stem(word))
            stem_sentence.append(" ")
        return "".join(stem_sentence)

    def stem_text(self, sentence: str) -> str:
        result = self.stem_sentence(sentence, self.stemmer)
        return result


"""
https://blog.mlreview.com/topic-modeling-with-scikit-learn-e80d33668730
--------> https://yanlinc.medium.com/how-to-build-a-lda-topic-model-using-from-text-601cdcbfd3a6 <--------
"""


class TopicAnalyzer:
    def __init__(self, texts, n_topics=None, n_jobs=-1, n_words=15, random_state=None):
        """
        Creates a class instance of the latent dirichlet analysis, which analyses topics
        :param texts: array of strings that the modeler should be trained on
        :param n_topics: count of how many topics it should divide the texts into, by default will try to find best from
                [10, 15, 20, 25, 30] if passed uses that instead
        :param n_jobs: how many cpu cores can be used, default is -1
        :param n_words: how many words related to a topic should be returned with a prediction
        :param random_state: random state for the lda model
        """
        self.raw_data = texts
        self.random_state = random_state
        self.n_words = n_words
        self.n_jobs = n_jobs
        self.lda_search_params = {'learning_decay': [.5, .7, .9]}
        if n_topics is not None:
            self.lda_search_params['n_components'] = [n_topics]
        else:
            self.lda_search_params['n_components'] = [10, 15, 20, 25, 30]
        self.vectorizer = CountVectorizer(analyzer='word',
                                          min_df=10,
                                          stop_words='english',
                                          lowercase=True,
                                          token_pattern='[a-zA-Z0-9]{3,}')

        self.lda_model = None
        self.vectorized = None
        self.lda_output = None
        self.best_lda_params = None
        self.df_topic_keywords = None
        self.ready = False

    def setup(self, skip_clearing=False):
        self.setup_vectorize()
        self.setup_lda()
        if not skip_clearing:  # mark it so GC can remove can clear it if needed
            self.raw_data = None
            self.vectorized = None
            self.lda_output = None

    def setup_vectorize(self):
        self.vectorized = self.vectorizer.fit_transform(self.raw_data)

    def setup_lda(self):
        if self.vectorized is None:
            raise ValueError("vectorized values not calculated yet, call setup_vectorize")

        lda = LatentDirichletAllocation(max_iter=5, learning_method='online', learning_offset=50.,
                                        random_state=self.random_state, n_jobs=self.n_jobs)
        model = GridSearchCV(lda, param_grid=self.lda_search_params)
        model.fit(self.vectorized)

        self.lda_model = model.best_estimator_
        self.best_lda_params = model.best_params_
        self.lda_output = self.lda_model.transform(self.vectorized)

        if 'n_components' in self.best_lda_params:
            self.n_words = self.best_lda_params['n_components']

        topic_keywords = self._show_topics()  # Topic - Keywords Dataframe
        self.df_topic_keywords = pd.DataFrame(topic_keywords)  # Assign Column and Index
        self.ready = True

    def _show_topics(self):
        vectorizer = self.vectorizer
        lda_model = self.lda_model
        keywords = np.array(vectorizer.get_feature_names())
        topic_keywords = []
        for topic_weights in lda_model.components_:
            top_keyword_locs = (-topic_weights).argsort()[:self.n_words]
            topic_keywords.append(keywords.take(top_keyword_locs))

        return topic_keywords

    def predict(self, text):
        if not self.ready:
            raise Exception("Setup not yet complete, call setup function first.")

        data = [text]

        transformed = self.vectorizer.transform(data)
        topic_probability_scores = self.lda_model.transform(transformed)
        # get top N words from keywords
        topics = self.df_topic_keywords.iloc[np.argmax(topic_probability_scores), 1:(self.n_words-1)].values.tolist()
        dominant_topic_index = np.argmax(topic_probability_scores)
        dominant_topic = self.df_topic_keywords.iloc[dominant_topic_index, -1]
        return topics, dominant_topic, dominant_topic_index, topic_probability_scores[0]


class MLTextProcessingHelper:

    def __init__(self):
        # device = "cuda:0" if torch.cuda.is_available() else "cpu" #
        # https://discuss.huggingface.co/t/is-transformers-using-gpu-by-default/8500
        device = 0 if torch.cuda.is_available() else -1  # expects device id or -1 https://huggingface.co/transformers/main_classes/pipelines.html
        self.zero_short_model = pipeline(CLASSIFICATION_TASKS.ZERO_SHOT.value, CLASSIFICATION_MODELS.BART_LARGE.value,
                                         device=device)
        self.sentiment_classifier = pipeline(CLASSIFICATION_TASKS.SENTIMENT_ANALYSIS.value, device=device)

    def zeroshot_analysis(self, text, config):
        result = {}

        for key, value in config.zeroshot_configs.items():
            # value == ZeroshotConfig class
            try:
                if text == "":
                    print("Warning, no text to do zeroshot analysis")
                    result[key] = "NO LABEL"
                else:
                    result[key] = self.zeroshot_single_analysis(text, value.labels)['labels'][0]
            except:
                result[key] = "NO LABEL"
                print(f"Warning failed to do zeroshot analysis on <{text}>")

        return result

    def add_zeroshot_to_df(self, df, text_fields, config):
        total = len(df.shape[0])
        i = 0
        for index, row in df.iterrows():
            texts = [row[textField] for textField in text_fields]
            text = " ".join(texts)
            analysis = self.zeroshot_analysis(text, config)
            for name, values in analysis.items():
                if name not in df.columns:
                    df[name] = ""
                df[name][index] = values
            print(f"\rStatus: {i}/{total}", sep=' ', end='', flush=True)
            i = i+1

        return df

    def add_ml_generated_cols_to_df(self, df, text_fields, config: ConfigHelper):
        sentiment_key = "_sentiment"
        df = df.copy()
        total = len(df.index)

        if sentiment_key not in df.columns and config.sentiment_analysis:
            df[sentiment_key] = ""

        i=0
        for index, row in df.iterrows():
            texts = [row[textField] for textField in text_fields]
            text = " ".join(texts)
            if config.sentiment_analysis:
                sentiment = self.sentiment_analysis(text)
                df["_sentiment"][index] = sentiment
            if config.zeroshot_configs is not None:
                analysis = self.zeroshot_analysis(text, config)
                for name, values in analysis.items():
                    if name not in df.columns:
                        df[name] = ""
                    df[name][index] = values
            print(f"\rStatus: {i}/{total} ", sep=' ', end='', flush=True)
            i = i + 1
        return df

    def add_sentiment_to_df(self, df, text_fields):
        for index, row in df.iterrows():
            texts = [row[textField] for textField in text_fields]
            text = " ".join(texts)
            analysis = self.sentiment_analysis(text)
            df["_sentiment"][index] = analysis

        return df

    def zeroshot_single_analysis(self, text, labels):
        return self.zero_short_model(text, labels)

    def sentiment_analysis(self, text):
        try:
            classification = self.sentiment_classifier(text)
        except:
            classification = "NO LABEL"
            print(f"Warning sentiment analysis failed on <{text}>")
            return classification

        return classification[0]["label"] if len(classification) > 0 else ""
