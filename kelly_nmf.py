import pandas as pd
import numpy as np
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import CountVectorizer
from rob import get_content

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

    vectorizer = CountVectorizer(stop_words='english')
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
