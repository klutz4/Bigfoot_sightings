import pandas as pd
import numpy as np
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import CountVectorizer
from rob import get_content
from nltk.corpus import stopwords

def get_top_words(H,data):
    top_words = {}
    for i in range(H.shape[0]):
        top_words.setdefault(i, [])
        indices = np.argsort(H[i])[::-1]
        top_ten = indices[:10]
        for idx in top_ten:
            top_words[i].append(data[idx])
    return top_words

def top_three_topics_per_doc(doc, idx,data,W):
    top_three = np.argsort(W[idx])[::-1][:3]
    return top_three

if __name__ == '__main__':
    content = get_content()

    stopwords = set(stopwords.words('english'))
    for word in ['also','would','could','saw','report','bfro','like','said']:
        stopwords.add(word)
    vectorizer = CountVectorizer(stop_words=stopwords)
    td_mat = vectorizer.fit_transform(content)
    V = td_mat.toarray()
    feature_names = vectorizer.get_feature_names()
    k = 5

    nmf = NMF(n_components=k)
    nmf.fit(V)
    W = nmf.transform(V)
    H = nmf.components_
    err = nmf.reconstruction_err_

    #top words per topic
    top_words = get_top_words(H,feature_names)

    for idx in np.random.randint(0,4857,10):
        doc1 = content[idx]
        top_three = top_three_topics_per_doc(doc1,idx,content,W)
        print(idx,top_three)

#top words per topic
# {0: ['back', 'one', 'see', 'time', 'around', 'feet', 'got', 'looked', 'us', 'something'],
# 1: ['heard', 'sound', 'night', 'area', 'sounds', 'time', 'woods', 'around', 'loud', 'camp'],
# 2: ['witness', 'animal', 'investigator', 'sighting', 'creature', 'woods', 'feet', 'hair', 'area', 'witnesses'],
# 3: ['road', 'creature', 'side', 'sighting', 'car', 'county', 'time', 'area', 'sightings', 'driving'],
# 4: ['area', 'tracks', 'found', 'large', 'trail', 'one', 'deer', 'creek', 'tree', 'lake']}

# top three topics per report examples
# 3962 [3 0 2]
# 3619 [0 2 3]
# 1018 [2 3 4]
# 2967 [1 0 4]
# 4500 [1 3 4]
# 734 [3 4 2]
# 55 [2 1 3]
# 1025 [3 4 2]
# 3675 [2 0 1]
# 3932 [2 3 0]
