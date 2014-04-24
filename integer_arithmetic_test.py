import unittest
from integer_arithmetic import catalan_number_count_iterative, catalan_number_count_rec

class CatalanNumberTest(unittest.TestCase):
  def test_catalan_number(self):
    self.assertEqual(catalan_number_count_rec(0), 1)
    self.assertEqual(catalan_number_count_rec(1), 1)
    self.assertEqual(catalan_number_count_rec(2), 2)
    self.assertEqual(catalan_number_count_rec(3), 5)

    for i in range(0, 10):
      self.assertEqual(catalan_number_count_iterative(i), catalan_number_count_rec(i))

if __name__ == "__main__":
  unittest.main()