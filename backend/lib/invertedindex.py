from typing import List, Dict
from collections import defaultdict
from lib.preprocessor import Preprocessor, preprocess
from lib.utils import contains
import bisect


class InvertedIndex:
    n: int = 0
    index: Dict[str, List[int]] = defaultdict(list)
    p: Preprocessor = None

    def __init__(self, p: Preprocessor):
        self.p = p

    def add(self, document: str):
        for tkn in self.p.clean_text(document):
            if not contains(self.index[tkn], self.n):
                bisect.insort(self.index[tkn], self.n)
        self.n += 1

    @preprocess
    def retrieve(self, word: str) -> List[int]:
        return self.index[word]

    def dump(self, filename: str):
        with open(filename, 'w') as f:
            for k, v in self.index.items():
                f.write(f"{k}: {','.join([str(x) for x in v])}\n")
