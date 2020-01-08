import nltk, string, numpy
from sklearn.feature_extraction.text import TfidfVectorizer

from gensim.matutils import softcossim
from gensim import corpora
import gensim.downloader as api

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
def cos_similarity(textlist):
    tfidf = TfidfVec.fit_transform(textlist)
    return (tfidf * tfidf.T).toarray()[0][1]

def text_similarity(documents):
    x = int(cos_similarity(documents)*100)
    return x
