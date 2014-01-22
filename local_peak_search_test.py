import unittest
from local_peak_search import *

class TestLocalPeakSearch(unittest.TestCase):
  def setUp(self):
    self.seq = []
    self.seq.append(([3], [3]))
    self.seq.append(([3,4], [4]))
    self.seq.append(([5,4], [5]))
    self.seq.append(([1,3,45,2,3,6,7,4], [7,45]))
    self.seq.append(([100,3,45,2,30,6,70,4], [100,45,40,70]))

  def test_naive_search(self):
    for s in self.seq:
      self.assertIn(naive_search(s[0]), s[1])

  def test_divide_and_conquer_search(self):
    for s in self.seq:
      self.assertIn(divide_and_conquer_search(s[0]), s[1])

if __name__ == '__main__':
  unittest.main()