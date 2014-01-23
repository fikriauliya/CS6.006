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

class Test2DLocalPeakSearch(unittest.TestCase):
  def setUp(self):
    self.seq = []
    self.seq.append(([[1]], [1]))
    self.seq.append(([[1,2],[3,1]], [2,3]))
    self.seq.append(([[1,2,4],[3,1,5]], [3,4,5]))
    self.seq.append(([[1,1,1],[1,1,2]], [2]))
    self.seq.append(([[1,1,1],[1,1,1]], [1]))
    self.seq.append(([[1,1,1,5],[1,1,1,8],[1,1,1,10]], [10]))

  def test_naive_2d_search(self):
    for s in self.seq:
      self.assertIn(naive_2d_search(s[0]), s[1])

  def test_divide_and_conquer_2d_search(self):
    for s in self.seq:
      self.assertIn(divide_and_conquer_2d_search(s[0]), s[1])

if __name__ == '__main__':
  unittest.main()