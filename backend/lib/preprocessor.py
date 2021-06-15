from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
import string


class Preprocessor:
    stemmer = SnowballStemmer('spanish')
    stop = stopwords.words('spanish')

    def __init__(self):
        pass

    def valid(self, token: str):
        return token not in self.stop and token not in string.punctuation

    def clean(self, word: str):
        return self.stemmer.stem(word.lower())

    def clean_text(self, document: str):
        tokens = word_tokenize(document)
        return [self.clean(tkn) for tkn in tokens if self.valid(tkn)]


def preprocess(f):
    def wrapper(instance, *args):
        return f(
            instance, *[
                instance.p.clean(str(arg)) if type(arg) is str else arg
                for arg in list(args)
            ])

    return wrapper
