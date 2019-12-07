from main_4 import inputs
import unittest
from math import exp, sqrt

e = 0.00001


class TestCalc(unittest.TestCase):
    def test_0(self):
        res = inputs("x**3 + y**3 - 3*x*y", [0, 0], [0, 1], [1, 0], 34)
        self.assertTrue(abs(res[0][0] - 1) < e and abs(res[0][1] - 1) < e and abs(res[1] + 1) < e)

    def test_1(self):
        res = inputs("5*(x - 3)**2 + (y - 5)**2", [2, 6], [4, 4], [4, 3], 19)
        self.assertTrue(abs(res[0][0] - 3) < e and abs(res[0][1] - 5) < e and abs(res[1]) < e)

    def test_2(self):
        res = inputs("x**2 + y**2 + x*y", [1, 1], [0, 1], [1, 0], 2)
        self.assertTrue(abs(res[0][0]) < e and abs(res[0][1]) < e and abs(res[1]) < e)

    def test_3(self):
        res = inputs("(x-5)**2 + (y+3)**2 - 7", [4, -2], [5, -2], [5, -4], 42)
        self.assertTrue(abs(res[0][0] - 5) < e and abs(res[0][1] + 3) < e and abs(res[1] + 7) < e)


if __name__ == "__main__":
    unittest.main()
