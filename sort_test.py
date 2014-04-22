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
    self.testcases.append(([329,457,657,839,436,720,355], [329,355,436,457,657,720,839]))
    self.testcases.append(([329,457,657,839,436,720,355,10000], [329,355,436,457,657,720,839,10000]))
    self.testcases.append(([329,457,657,839,436,720,355,-10000], [-10000,329,355,436,457,657,720,839]))

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

  def test_counting_sort(self):
    for t in self.testcases:
      self.assertEqual(counting_sort(t[0],-10000,10000), t[1])

  def test_counting_sort_with_key(self):
    for t in self.testcases:
      self.assertEqual(counting_sort_with_key(t[0], lambda x:x, -10000, 10000), t[1])

  def test_radix_sort(self):
    for t in self.testcases:
      self.assertEqual(radix_sort(t[0], 10), t[1])

if __name__ == "__main__":
  unittest.main()