import unittest
import math

from integer_arithmetic import *

class CatalanNumberTest(unittest.TestCase):
  def test_catalan_number(self):
    self.assertEqual(catalan_number_count_rec(0), 1)
    self.assertEqual(catalan_number_count_rec(1), 1)
    self.assertEqual(catalan_number_count_rec(2), 2)
    self.assertEqual(catalan_number_count_rec(3), 5)

    for i in range(0, 10):
      self.assertEqual(catalan_number_count_iterative(i), catalan_number_count_rec(i))

class CommonArithmeticTest(unittest.TestCase):
  def test_square_root(self):
    self.assertEqual(square_root(2, 0), 1)
    self.assertEqual(square_root(2, 1), 1.5)
    self.assertEqual(square_root(2, 10), square_root(2, 11))
    self.assertEqual(round(square_root(2, 10), 10), round(math.sqrt(2), 10))

  def test_multiply(self):
    self.assertEqual(multiply(2, 4), 8)
    self.assertEqual(multiply(3, 3), 9)
    self.assertEqual(karatsuba_multiply(-3, -3), 9)
    self.assertEqual(multiply(11, 11), 121)
    self.assertEqual(multiply(121, 11), 11*121)
    self.assertEqual(multiply(12100, 11), 11*12100)
    self.assertEqual(multiply(12100, 2), 2*12100)
    self.assertEqual(multiply(12100, -2), -2*12100)
    self.assertEqual(multiply(-12100, -2), -2*-12100)

  def test_karatsuba_multiply(self):
    self.assertEqual(karatsuba_multiply(2, 4), 8)
    self.assertEqual(karatsuba_multiply(3, 3), 9)
    self.assertEqual(karatsuba_multiply(-3, -3), 9)
    self.assertEqual(karatsuba_multiply(11, 11), 121)
    self.assertEqual(karatsuba_multiply(121, 11), 11*121)
    self.assertEqual(karatsuba_multiply(12100, 11), 11*12100)
    self.assertEqual(karatsuba_multiply(12100, 2), 2*12100)
    self.assertEqual(karatsuba_multiply(12100, -2), -2*12100)
    self.assertEqual(karatsuba_multiply(-12100, -2), -2*-12100)

if __name__ == "__main__":
  unittest.main()