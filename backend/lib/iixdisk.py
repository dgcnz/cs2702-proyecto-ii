from typing import List
from functools import reduce
from math import log
from math import sqrt
from pathlib import Path
from lib.preprocessor import clean_text
from collections import defaultdict
import os
import json


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class DiskInvertedIndex:
    N: int  # Number of documents
    indexpath: Path = Path('index')
    datapath: Path
    iixpath: Path
    normpath: Path
    idfpath: Path

    def __init__(self, datapath: Path, cached=False):
        self.datapath = datapath
        files = list(self.datapath.glob('*.json'))
        self.N = len(files)  # Number of documents
        if not cached:
            B = int(self.N / log(self.N))  # Number of documents per block

            blocks = map(lambda args: self.block_process(*args),
                         enumerate(chunks(files, B)))
            self.iixpath = reduce(self.block_merge, list(blocks))
            self.iixpath.rename(self.indexpath / 'iix.json')
            self.iixpath = self.indexpath / 'iix.json'
            self.precompute()
        else:
            self.iixpath = self.indexpath / 'iix.json'
            self.normpath = self.indexpath / 'norm.json'
            self.idfpath = self.indexpath / 'idf.json'

    def load_iix(self, iixpath: Path):
        data = {}
        with open(iixpath, 'r') as f:
            data = json.load(f)

        return defaultdict(lambda: defaultdict(float),
                           {k: defaultdict(float, v)
                            for k, v in data.items()})

    def save_iix(self, iixpath: Path, iix):
        for k in iix.keys():
            iix[k] = sorted(list(iix[k].items()))
        with open(iixpath, 'w') as f:
            json.dump(iix, f)

    def precompute(self):
        data = self.load_iix(self.iixpath)
        idf = defaultdict(float)
        norm = defaultdict(float)
        for word, doc_cnts in data.items():
            idf[word] += len(doc_cnts)

        for word in idf.keys():
            idf[word] = log(self.N / idf[word])

        for word, doc_cnts in data.items():
            for docid, cnt in doc_cnts.items():
                docid = int(docid)
                data[word][docid] = log(1 + cnt) * idf[word]
                norm[docid] += data[word][docid]**2

        for docid in norm.keys():
            docid = int(docid)
            norm[docid] = sqrt(norm[docid])

        self.normpath = self.indexpath / 'norm.json'
        self.idfpath = self.indexpath / 'idf.json'
        self.save_iix(self.iixpath, data)
        with open(self.normpath, 'w') as f:
            json.dump(norm, f)
        with open(self.idfpath, 'w') as f:
            json.dump(idf, f)

    def block_process(self, block_id, filenames: List[Path]) -> Path:
        iix = defaultdict(lambda: defaultdict(int))

        for filename in filenames:
            with open(filename, 'r') as f:
                docid = int(filename.stem)
                data = json.load(f)
                for word in clean_text(data['content']):
                    iix[word][docid] += 1

        filename = self.indexpath / f'{block_id}.json'
        self.save_iix(filename, iix)
        return filename

    def block_merge(self, block0: Path, block1: Path) -> Path:
        if block0 is None:
            return block1
        if block1 is None:
            return block0
        data0 = self.load_iix(block0)
        data1 = self.load_iix(block1)
        merged = defaultdict(lambda: defaultdict(int))
        for word, docid_cnts in data0.items():
            for docid, cnt in docid_cnts.items():
                docid = int(docid)
                merged[word][docid] += cnt
        for word, docid_cnts in data1.items():
            for docid, cnt in docid_cnts.items():
                docid = int(docid)
                merged[word][docid] += cnt
        self.save_iix(block0, merged)
        os.remove(block1)
        return block0

    def load(self):
        iix = self.load_iix(self.iixpath)
        norm = {}
        with open(self.normpath, 'r') as f:
            norm = json.load(f)

        idf = {}
        with open(self.idfpath, 'r') as f:
            idf = json.load(f)

        return iix, norm, idf

    def query(self, qtext: str, k: int) -> List[Path]:
        iix, norm, idf = self.load()
        qtokens = clean_text(qtext)
        qtokens = list(filter(lambda qtoken: qtoken in idf.keys(), qtokens))
        wq = defaultdict(float)
        for qtoken in qtokens:
            wq[qtoken] += 1

        qnorm = 0.0
        for qtoken in wq.keys():
            wq[qtoken] = log(1 + wq[qtoken]) * idf[qtoken]
            qnorm += wq[qtoken]**2

        qnorm = sqrt(qnorm)
        for qtoken in wq.keys():
            wq[qtoken] /= qnorm

        score = defaultdict(float)
        for qtoken in qtokens:
            for docid, wt in iix[qtoken].items():
                docid = int(docid)
                score[docid] += wq[qtoken] * wt

        for docid, docnorm in norm.items():
            docid = int(docid)
            score[docid] /= docnorm

        ans = list(score.items())
        ans.sort(key=lambda x: x[1], reverse=True)
        ans = [(self.datapath / f'{x[0]}.json', x[1]) for x in ans]
        return ans[:k]
