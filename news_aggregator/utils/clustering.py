# news_aggregator/utils/clustering.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def perform_clustering(articles):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(articles)
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    kmeans.fit(X)
    
    return kmeans.labels_
