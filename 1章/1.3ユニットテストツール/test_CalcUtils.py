import unittest
from unittest import TestCase

from calc_utils import CalcUtils


class TestCalcUtils(TestCase):
    def test_squareが2乗の値を返すこと(self):
        self.assertEqual(CalcUtils.square(2), 2**2)


if __name__ == "__main__":
    unittest.main()
