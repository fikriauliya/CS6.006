import unittest
from dynamic_programming import *

class DynamicProgrammingTest(unittest.TestCase):
  def test_fibonacci(self):
    self.assertEqual(fibonacci(1), 1)
    self.assertEqual(fibonacci(2), 1)
    self.assertEqual(fibonacci(3), 2)
    self.assertEqual(fibonacci(4), 3)
    self.assertEqual(fibonacci(5), 5)
    self.assertEqual(fibonacci(6), 8)
    self.assertEqual(fibonacci(7), 13)
    self.assertEqual(fibonacci(8), 21)

  def test_fibonacci_memoization(self):
    self.assertEqual(fibonacci_memoization(1), 1)
    self.assertEqual(fibonacci_memoization(2), 1)
    self.assertEqual(fibonacci_memoization(3), 2)
    self.assertEqual(fibonacci_memoization(4), 3)
    self.assertEqual(fibonacci_memoization(5), 5)
    self.assertEqual(fibonacci_memoization(6), 8)
    self.assertEqual(fibonacci_memoization(7), 13)
    self.assertEqual(fibonacci_memoization(8), 21)
    self.assertEqual(fibonacci_memoization(100), 354224848179261915075)

  def test_fibonacci_bottom_up(self):
    self.assertEqual(fibonacci_bottom_up(1), 1)
    self.assertEqual(fibonacci_bottom_up(2), 1)
    self.assertEqual(fibonacci_bottom_up(3), 2)
    self.assertEqual(fibonacci_bottom_up(4), 3)
    self.assertEqual(fibonacci_bottom_up(5), 5)
    self.assertEqual(fibonacci_bottom_up(6), 8)
    self.assertEqual(fibonacci_bottom_up(7), 13)
    self.assertEqual(fibonacci_bottom_up(8), 21)
    self.assertEqual(fibonacci_bottom_up(100), 354224848179261915075)

if __name__ == "__main__":
  unittest.main()