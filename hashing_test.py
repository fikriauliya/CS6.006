import unittest
from hashing import *

class TestSort(unittest.TestCase):
  def test_put_and_get(self):
    hash = HashWithChaining(2)
    self.assertEqual(hash.get(1), None)

    hash.put(1, "one")
    hash.put(1, "uno")
    self.assertEqual(hash.get(1), (1, "uno"))

    hash.put(1, "satu")
    self.assertEqual(hash.get(1), (1, "satu"))

    hash.put(2, "dua")
    hash.put(2, "two")
    hash.put(3, "three")
    hash.put(3, "san")
    hash.put(4, "four")
    hash.put(5, "five")
    hash.put(6, "six")
    hash.put(7, "seven")
    hash.put(8, "eight")
    hash.put(9, "nine")
    hash.put(10, "ten")

    self.assertEqual(hash.get(2), (2, "two"))
    self.assertEqual(hash.get(3), (3, "san"))
    self.assertNotEqual(hash.get(3), (3, "three"))

    self.assertEqual(hash.hash_size(), 10)
    hash.remove(3)
    self.assertEqual(hash.get(3), None)
    self.assertEqual(hash.hash_size(), 9)

if __name__ == "__main__":
  unittest.main()