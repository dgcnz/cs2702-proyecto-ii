from typing import List
from lib.preprocessor import Preprocessor
from collections import Counter
import bisect


def OR(a: List[int], b: List[int]) -> List[int]:
    ans = []
    i: int = 0
    j: int = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        elif b[j] < a[i]:
            ans.append(b[j])
            j += 1
        else:
            ans.append(a[i])
            i += 1
            j += 1

    while i < len(a):
        ans.append(a[i])
        i += 1

    while j < len(b):
        ans.append(b[j])
        j += 1

    return ans


def AND(a: List[int], b: List[int]) -> List[int]:
    ans = []

    i: int = 0
    j: int = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            ans.append(a[i])
            i += 1
            j += 1
    return ans


def ANDNOT(a: List[int], b: List[int]) -> List[int]:
    ans = []

    i: int = 0
    j: int = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        elif b[j] < a[i]:
            j += 1
        else:
            i += 1
            j += 1

    while i < len(a):
        ans.append(a[i])
        i += 1

    return ans


# ************************** HELPERS ********************************


class CorpusStatistics:
    p: Preprocessor = None
    counter = Counter()

    def __init__(self, documents: List[str], p: Preprocessor):
        self.p = p
        for doc in documents:
            for tkn in p.clean_text(doc):
                self.counter[tkn] += 1

    def most_common(self, k: int) -> List[str]:
        return [word[0] for word in self.counter.most_common(k)]


def contains(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False
