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
    return matched_key_value_pair

  def remove(self, key):
    hashed_key = self.__hash(key)

    matched_key_value_index = next((index for index, key_value_pair
                                    in enumerate(self.hash_indices[hashed_key])
                                    if key_value_pair[0] == key), None)
    if matched_key_value_index != None:
      del self.hash_indices[hashed_key][matched_key_value_index]
      self.filled_size -= 1

  def hash_size(self):
    return self.filled_size