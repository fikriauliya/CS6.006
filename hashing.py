import sys

class HashWithChaining:
  def __init__(self, size=10000):
    self.filled_size = 0
    self.size = size
    self.hash_indices = [[] for _ in range(0, self.size)]

  @staticmethod
  def __pre_hash(key):
    return key.__hash__()

  def __hash(self, key):
    pre_hashed_key = HashWithChaining.__pre_hash(key)

    random_1 = 17933623
    random_2 = 86536918
    large_prime = 104395301
    return ((random_1 * pre_hashed_key + random_2) % large_prime) % self.size

  def put(self, key, value):
    if self.size == self.filled_size:
      new_table_doubling = HashWithChaining(self.size * 2)

      for hash_index in self.hash_indices:
        for key_value_pair in hash_index:
          new_table_doubling.put(key_value_pair[0], key_value_pair[1])

      self.size = self.size * 2
      self.hash_indices = new_table_doubling.hash_indices

    hashed_key = self.__hash(key)
    matched_key_value_index = next((index for index, key_value_pair
                                    in enumerate(self.hash_indices[hashed_key])
                                    if key_value_pair[0] == key), None)

    if matched_key_value_index == None:
      self.hash_indices[hashed_key].append((key, value))
      self.filled_size += 1
    else:
      self.hash_indices[hashed_key][matched_key_value_index] = (key, value)

  def get(self, key):
    hashed_key = self.__hash(key)

    matched_key_value_pair = next((key_value_pair for key_value_pair
                                   in self.hash_indices[hashed_key]
                                   if key_value_pair[0] == key), None)

    if matched_key_value_pair == None: return None
    return matched_key_value_pair[1]

  def remove(self, key):
    hashed_key = self.__hash(key)

    matched_key_value_index = next((index for index, key_value_pair
                                    in enumerate(self.hash_indices[hashed_key])
                                    if key_value_pair[0] == key), None)
    if matched_key_value_index != None:
      del self.hash_indices[hashed_key][matched_key_value_index]
      self.filled_size -= 1

      if self.filled_size <= self.size // 4:
        new_table_doubling = HashWithChaining(self.size // 2)

        for hash_index in self.hash_indices:
          for key_value_pair in hash_index:
            new_table_doubling.put(key_value_pair[0], key_value_pair[1])

        self.size = self.size // 2
        self.hash_indices = new_table_doubling.hash_indices

class HashWithOpenAddressing:
  DELETED_FLAG = sys.maxsize

  def __init__(self, size=10000):
    self.filled_size = 0
    self.size = size
    self.hash_values = [None for _ in range(0, self.size)]

  @staticmethod
  def __pre_hash(key):
    return key.__hash__()

  def __hash(self, key, counter):
    pre_hashed_key = HashWithOpenAddressing.__pre_hash(key)

    random_1 = 17933623
    random_2 = 86536918
    large_prime = 104395301
    return (((random_1 * pre_hashed_key + random_2) % large_prime) + counter) % self.size

  def put(self, key, value):
    for i in range(0, self.size):
      hashed_key = self.__hash(key, i)
      if self.hash_values[hashed_key] == None or self.hash_values[hashed_key] == HashWithOpenAddressing.DELETED_FLAG:
        self.hash_values[hashed_key] = (key, value)
        self.filled_size += 1
        return
      elif self.hash_values[hashed_key][0] == key:
        # overwrite
        self.hash_values[hashed_key] = (key, value)
        return

    raise Exception("Hash full")

  def get(self, key):
    for i in range(0, self.size):
      hashed_key = self.__hash(key, i)
      if self.hash_values[hashed_key] == HashWithOpenAddressing.DELETED_FLAG: continue
      if self.hash_values[hashed_key] == None: return None
      elif self.hash_values[hashed_key][0] == key:
        return self.hash_values[hashed_key][1]

    return None

  def remove(self, key):
    for i in range(0, self.size):
      hashed_key = self.__hash(key, i)
      if self.hash_values[hashed_key] == HashWithOpenAddressing.DELETED_FLAG: continue
      if self.hash_values[hashed_key] == None: return
      elif self.hash_values[hashed_key][0] == key:
        self.hash_values[hashed_key] = HashWithOpenAddressing.DELETED_FLAG
        self.filled_size -= 1
        return