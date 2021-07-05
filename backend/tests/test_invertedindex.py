import unittest
from pathlib import Path
from lib.iixdisk import DiskInvertedIndex


class TestInvertedIndex(unittest.TestCase):
    def test_cached_query(self):
        iix = DiskInvertedIndex(Path('data/'), False)  # change this to true
        ans = iix.query(
            'After the bullet shells get counted, the blood dries and the votive candles burn',
            10)
        best = Path('data/17284.json')
        print(ans, best in ans)
        self.assertEqual(ans[0][0], best)


if __name__ == '__main__':
    unittest.main(verbosity=2)
