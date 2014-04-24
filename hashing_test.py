import unittest
from hashing import *

class TestSort(unittest.TestCase):
  def test_hash_with_chaining(self):
    hash = HashWithChaining(2)
    self.assertEqual(hash.get(1), None)

    hash.put(1, "one")
    hash.put(1, "uno")
    self.assertEqual(hash.get(1), "uno")

    hash.put(1, "satu")
    self.assertEqual(hash.get(1), "satu")

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

    self.assertEqual(hash.get(2), "two")
    self.assertEqual(hash.get(3), "san")
    self.assertNotEqual(hash.get(3), "three")

    self.assertEqual(hash.filled_size, 10)
    self.assertEqual(hash.size, 16)
    hash.remove(3)
    self.assertEqual(hash.get(3), None)
    self.assertEqual(hash.filled_size, 9)
    self.assertEqual(hash.size, 16)

    hash.remove(1)
    hash.remove(2)
    self.assertEqual(hash.filled_size, 7)
    self.assertEqual(hash.size, 16)

    hash.remove(7)
    hash.remove(8)
    hash.remove(9)
    self.assertEqual(hash.filled_size, 4)
    self.assertEqual(hash.size, 8)

  def test_hash_with_open_addressing(self):
    hash = HashWithOpenAddressing(4)
    self.assertEqual(hash.size, 4)

    hash.put(1, "one")
    hash.put(1, "uno")
    self.assertEqual(hash.get(1), "uno")
    self.assertEqual(hash.filled_size, 1)

    hash.put(2, "two")
    self.assertEqual(hash.get(2), "two")
    self.assertEqual(hash.filled_size, 2)

    hash.remove(1)
    self.assertEqual(hash.get(1), None)
    self.assertEqual(hash.filled_size, 1)

    hash.remove(23)
    self.assertEqual(hash.filled_size, 1)

    hash.put(1, "one")
    self.assertEqual(hash.get(1), "one")
    self.assertEqual(hash.filled_size, 2)

    hash.put(3, "three")
    hash.put(4, "four")
    with self.assertRaises(Exception):
      hash.put(5, "five")

  def test_hash_with_open_addressing_probing(self):
    hash_1 = HashWithOpenAddressing(100)
    for i in range(0,100):
      hash_1.put(i*2, i)
    with self.assertRaises(Exception):
      hash_1.put(1, "helo")

if __name__ == "__main__":
  unittest.main()