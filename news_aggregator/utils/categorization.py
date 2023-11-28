# news_aggregator/utils/categorization.py

from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer

def perform_categorization(articles, categories):
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    model.fit(articles, categories)
    return model.predict(articles)
