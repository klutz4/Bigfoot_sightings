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

big_foot_sw = ['report','area','bfro','witness','saw','time','heard','road','2007','2008','like','animal','sound'
'location','town','details','observed','date','noticed','year','month','date']
stopwords.extend(big_foot_sw)
new = set(stopwords)


#Vectorize
n_clusters = 5
vectorizer = TfidfVectorizer(stop_words=new,max_features=1000)
X = vectorizer.fit_transform(data)
features = vectorizer.get_feature_names()
kmeans = KMeans(n_clusters)
kmeans.fit(X)
top_centroids = kmeans.cluster_centers_.argsort()[:,-1:-11:-1]
print("\n4) top features for each cluster with 1000 max features:")
for num, centroid in enumerate(top_centroids):
    print("%d: %s" % (num, ", ".join(features[i] for i in centroid)))

#
'''
Unlimited Clusters

0: sound, sounds, lake, scream, howl, loud, night, vocalizations, expedition, sounded
1: tracks, prints, snow, track, print, found, inches, foot, footprints, trail
2: creature, sighting, car, driving, highway, hair, side, tall, feet, said
3: florida, expedition, north, creature, michigan, georgia, woods, investigator, 2009, 2013
4: house, window, woods, back, night, dogs, one, around, said, door
5: stan, courtney, illinois, see, collected, giving, audio, special, recording, com
6: river, back, could, tree, see, us, one, would, woods, said
7: camp, tent, night, lake, camping, us, around, fire, back, sound


Limited to 5 Clusters

0: tracks, prints, snow, track, print, found, inches, footprints, foot, trail
1: stan, courtney, illinois, see, collected, giving, audio, special, recording, com
2: florida, expedition, michigan, 2013, 2012, creature, north, investigator, woods, expeditions
3: sound, night, lake, camp, sounds, tent, one, us, back, loud
4: creature, back, sighting, said, see, one, feet, around, could, hair
'''
