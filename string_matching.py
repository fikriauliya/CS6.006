import sys

class RollingHash:
  def __init__(self):
    self.data = 0
    self.base = 256
    self.modulo = sys.maxsize
    self.length = 0

  def append(self, char):
    self.data = ((self.data % self.modulo) * self.base + ord(char)) % self.modulo
    self.length += 1

  def skip(self, char):
    self.data = ((self.data % self.modulo) - ord(char) * ((self.base ** (self.length - 1))) % self.modulo) % self.modulo
    self.length -= 1

  def value(self):
    return self.data

class StringMatching:
  # O(|s|.|t|)
  @staticmethod
  def simple_matching(substring, text):
    return any([substring == text[i:i+len(substring)]
                for i in range(0, len(text)-len(substring) + 1)])


  @staticmethod
  def karp_rabin(substring, text):
    substring_hash = RollingHash()
    text_hash = RollingHash()

    for c in substring: substring_hash.append(c)
    for c in text[:len(substring)]: text_hash.append(c)

    if substring_hash.value() == text_hash.value(): return True

    for i in range(len(substring), len(text)):
      text_hash.skip(text[i - len(substring)])
      text_hash.append(text[i])
      if substring_hash.value() == text_hash.value(): return True

    return False