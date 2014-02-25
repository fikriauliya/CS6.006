import unittest
from sort import *

class TestSort(unittest.TestCase):
  def setUp(self):
    self.testcases = []
    self.testcases.append(([], []))
    self.testcases.append(([1], [1]))
    self.testcases.append(([1,2], [1,2]))
    self.testcases.append(([2,1], [1,2]))
    self.testcases.append(([3,2,1], [1,2,3]))
    self.testcases.append(([3,3,2,1], [1,2,3,3]))
    self.testcases.append(([-100,-99,-98,-100,100], [-100,-100,-99,-98,100]))

  def test_insertion_sort(self):
    for t in self.testcases:
      self.assertEqual(insertion_sort(t[0]), t[1])

  def test_merged_sort(self):
    for t in self.testcases:
      self.assertEqual(merge_sort(t[0]), t[1])

  def test_heap_sort(self):
    for t in self.testcases:
      self.assertEqual(min_heap_sort(t[0]), t[1])

  def test_binary_search_tree_sort(self):
    for t in self.testcases:
      self.assertEqual(binary_search_tree_sort(t[0]), t[1])

if __name__ == "__main__":
  unittest.main()