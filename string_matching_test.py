import unittest
from string_matching import *

class StringMatchingTest(unittest.TestCase):
  def setUp(self):
    self.input_to_expecteds = []
    self.input_to_expecteds.append((["Hello", "Hello"], True))
    self.input_to_expecteds.append((["Hello", "Hello World"], True))
    self.input_to_expecteds.append((["Hello", "Helo World"], False))
    self.input_to_expecteds.append((["abbabc", "sdabbabcsd"], True))
    self.input_to_expecteds.append((["abbabc", "sdabbaBcsd"], False))

  def test_simple_matching(self):
    for input_to_expected in self.input_to_expecteds:
      self.assertEqual(StringMatching.simple_matching(*input_to_expected[0]), input_to_expected[1])

  def test_karp_rabin(self):
    for input_to_expected in self.input_to_expecteds:
      observed = StringMatching.karp_rabin(*input_to_expected[0])
      self.assertEqual(observed, input_to_expected[1])

if __name__ == '__main__':
  unittest.main()