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
    for word in ['also','would','could','saw','report','bfro','like','said','YEAR', 'SEASON', 'MONTH', 'STATE', 'COUNTY', 'LOCATION DETAILS', 'NEAREST TOWN', 'NEAREST ROAD', 'OBSERVED', 'ALSO NOTICED', 'OTHER WITNESSES', 'OTHER STORIES', 'TIME AND CONDITIONS', 'ENVIRONMENT']:
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
 # {0: ['back', 'see', 'one', 'creature', 'time', 'feet', 'looked', 'around', 'hair', 'something'],
 # 1: ['road', 'creature', 'side', 'sighting', 'car', 'driving', 'see', 'time', 'highway', 'feet'],
 # 2: ['woods', 'investigator', 'expedition', 'county', 'witnesses', 'year', 'sightings', 'net', 'near', 'animal'],
 # 3: ['night', 'us', 'sound', 'lake', 'camp', 'time', 'one', 'back', 'around', 'sounds'],
 # 4: ['tracks', 'found', 'snow', 'track', 'one', 'trail', 'prints', 'foot', 'inches', 'large']}
