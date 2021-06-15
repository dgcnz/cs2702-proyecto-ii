from typing import List, Dict, Set
from collections import defaultdict
from lib.preprocessor import Preprocessor, preprocess
from lib.utils import OR, AND, ANDNOT, contains, CorpusStatistics
from lib.parse import get_parser, execute
import bisect


class InvertedIndex:
    n: int = 0
    index: Dict[str, List[int]] = defaultdict(list)
    indexed_words: Set[str] = {}
    p: Preprocessor = None

    def __init__(self, indexed_words: List[str], p: Preprocessor):
        self.indexed_words = set(indexed_words)
        self.p = p

    def add(self, document: str):
        for tkn in self.p.clean_text(document):
            if tkn in self.indexed_words and not contains(
                    self.index[tkn], self.n):
                bisect.insort(self.index[tkn], self.n)
        self.n += 1

    @preprocess
    def retrieve(self, word: str) -> List[int]:
        if word in self.indexed_words:
            return self.index[word]
        return []

    def query(self, q: str) -> List[int]:
        """ Query Inverted Index in natural language
        Example: OR(RET(word1), AND(RET(word2), RET(word3)))
        """
        functions = {
            'RET': lambda word: self.retrieve(word),
            'OR': lambda a, b: OR(a, b),
            'AND': lambda a, b: AND(a, b),
            'ANDNOT': lambda a, b: ANDNOT(a, b)
        }
        parser = get_parser()
        ast = list(parser.parseString(q))
        result = execute(ast, functions)
        return result[0]

    def dump(self, filename: str):
        with open(filename, 'w') as f:
            for k, v in self.index.items():
                f.write(f"{k}: {','.join([str(x) for x in v])}\n")


def build_inverted_index(documents: List[str], p: Preprocessor, k: int):
    stat = CorpusStatistics(documents, p)
    indexed_words = stat.most_common(k)
    iix = InvertedIndex(indexed_words, p)
    for doc in documents:
        iix.add(doc)
    return iix
