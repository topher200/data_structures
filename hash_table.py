#!/usr/bin/python3

from element import Element

num_buckets = 100

class HashTable():
  def __init__(self):
    self.table = []
    for i in range(num_buckets):
      self.table.append([])

  def add(self, element):
    self.table[self._hash_function(element.key)].append(element)

  def find(self, key):
    for element in self.table[self._hash_function(key)]:
      if element.key == key:
        return element

  # outputs all buckets with all elements
  def print(self):
    for i, bucket in enumerate(self.table):
      print('{0}:'.format(i), end = '')
      [print(element.output(), end='') for element in bucket]
      print()

  @staticmethod
  def _hash_function(string):
    # Coverts each char of string to an ordinal number, then sums them and mods
    # by the number of buckets
    return sum(map(ord, string)) % num_buckets
