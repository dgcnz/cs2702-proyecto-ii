import unittest
import glob
from lib.invertedindex import build_inverted_index
from lib.preprocessor import Preprocessor


class TestInvertedIndex(unittest.TestCase):
    def test_nested_query(self):
        """Test Nested Query"""
        files = glob.glob("tests/data/*.txt")
        files.sort()
        docs = []
        for file in files:
            with open(file, 'r') as f:
                docs.append(f.read())

        p = Preprocessor()
        iix = build_inverted_index(docs, p, 100)
        QUERY = "OR(AND(RET(frodo), RET(comunidad)), RET(mordor))"
        self.assertEqual(iix.query(QUERY), [1, 3, 4])


if __name__ == '__main__':
    unittest.main(verbosity=2)
