import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# content = get_content()

def cluster_text(data,stopwords):
    vectorizer = TfidfVectorizer(stop_words=stopwords, max_df=0.5, min_df=0.1, lowercase=True,max_features=100)
    tfidf_model = vectorizer.fit_transform(data)

    kmeans = KMeans(n_clusters=5).fit(tfidf_model)
    centroids = kmeans.cluster_centers_

    for cluster in centroids:
        sorted_cluster = sorted(cluster,reverse=True)
        top_ten = sorted_cluster[:10]
        indices = np.argsort(cluster)[::-1][:10]
        names = []
        for idx in indices:
            names.append(vectorizer.get_feature_names()[idx])
        # print(names)
    return vectorizer, tfidf_model, kmeans

stopwords = set(stopwords.words('english'))
for word in ['also','would','could','saw','report','bfro','like','said','YEAR', 'SEASON', 'MONTH', 'STATE', 'COUNTY', 'LOCATION','DETAILS', 'TOWN', 'NEAREST','ROAD', 'OBSERVED', 'NOTICED', 'OTHER','WITNESSES', 'STORIES', 'TIME', 'CONDITIONS', 'ENVIRONMENT']:
        stopwords.add(word)
vectorizer, tfidf_model, kmeans = cluster_text(content, stopwords)
sim = pdist(tfidf_model.toarray())
sim_matrix = squareform(sim)
hierarchies = linkage(sim,'average')
dendro = dendrogram(hierarchies)
plt.savefig('images/dendrogram_average.png')
plt.show()
