from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
stem = ps.stem

def getQueryVector(searchQuery):
    vector = {}
    for token in searchQuery:
        if token in stopwords:
            continue
        token = stem(token)
        if token in vector.keys():
            vector[token] += 1
        else:
            vector[token] = 1
    return vector

def getQueryVector(searchQuery):
    vector = {}
    for token in searchQuery:
        token = stem(token)
        if token in vector.keys():
            vector[token] += 1
        else:
            vector[token] = 1
    return vector
