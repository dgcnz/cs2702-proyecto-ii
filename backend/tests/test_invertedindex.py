import unittest
from pathlib import Path
from lib.iixdisk import DiskInvertedIndex


class TestInvertedIndex(unittest.TestCase):
    def test_cached_query(self):
        iix = DiskInvertedIndex(Path('data/'), True)
        ans = iix.query(
            'After the bullet shells get counted, the blood dries and the votive candles burn',
            10)
        print(ans)
        self.assertEqual(ans[0][0], Path('data/17284.json'))

    # def test_literal_query(self):
    #     iix = DiskInvertedIndex(Path('data/'))
    #     ans = iix.query(
    #         'After the bullet shells get counted, the blood dries and the votive candles burn',
    #         10)
    #     print(ans)
    #     self.assertEqual(ans[0][0], Path('data/17284.json'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
