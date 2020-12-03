from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import csv
import pandas as pd
import re
import nltk
import joblib

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')


class Predictor:
    def __init__(self):
        self.model = joblib.load("my_pipeline.joblib")
        self.tokeniser = nltk.tokenize.RegexpTokenizer(r'\w+')
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))
    # need to add title into this bitch

    def input_tokenisation(self, par):
        tmp = []
        if "(Reuters) - " in par:
            par = par.split(" - ")[1]
        sentences = nltk.sent_tokenize(par)
        for sent in sentences:
            sent = sent.lower()
            tokens = self.tokeniser.tokenize(sent)
            filtered_words = [w.strip()
                              for w in tokens if w not in self.stop_words and len(w) > 1]
            tmp.extend(filtered_words)
            tmp = [self.lemmatizer.lemmatize(j) for j in tmp]
        tmp = ','.join(tmp)
        return tmp

    def read_data(self, request):
        # might have to change this to accomendate the string
        data = []
        foo = self.input_tokenisation(request)
        data.append(foo)
        # data.append(request.form['title'])
        # data.append(request.form['body'])
        return data

    def predict(self, request):
        prediction = self.model.predict(self.read_data(request))
        return prediction
