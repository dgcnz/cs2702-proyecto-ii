from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
import string

_stemmer = SnowballStemmer('english')
_stop = stopwords.words('english')


def valid(token: str):
    return token not in _stop and token not in string.punctuation


def clean_word(word: str):
    return _stemmer.stem(word.lower())


def clean_text(document: str):
    tokens = word_tokenize(document)
    return [clean_word(tkn) for tkn in tokens if valid(tkn)]
