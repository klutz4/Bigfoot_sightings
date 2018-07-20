#Rob NLP

import nltk
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import re
import numpy as np
from rob import get_content
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from sklearn.datasets import fetch_20newsgroups
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from nltk.corpus import stopwords

#Get data
data = np.array(get_content())


#Tokenize
porter = PorterStemmer()
snowball = SnowballStemmer('english')

def stem_text(stemmer,text_list):
    processed_tokens = []
    for i in text_list:
        for k in i:
            k = stemmer.stem(k)
            processed_tokens.append(k)
    return processed_tokens

new_content = stem_text(porter,data)
new_data = []
for i in new_content:
    temp = " ".join(i)
    new_data.append(temp)

stopwords =  stopwords.words('english')

big_foot_sw = ['report','area','bfro','witness','saw','time','heard']
stopwords.extend(big_foot_sw)
new = set(stopwords)


#Vectorize
vectorizer = TfidfVectorizer(stop_words=new)
X = vectorizer.fit_transform(data)
features = vectorizer.get_feature_names()
kmeans = KMeans()
kmeans.fit(X)
top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-11:-1]
print("\n4) top features for each cluster with 1000 max features:")
for num, centroid in enumerate(top_centroids):
    print("%d: %s" % (num, ", ".join(features[i] for i in centroid)))

#
