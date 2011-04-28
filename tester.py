#!/usr/bin/python3

import random
from element import Element
from hash_table import HashTable
import tree
import timeit

def generate_random_key():
  length = random.randint(1, 10)
  string_as_int_array = []
  for _ in range(length):
    string_as_int_array.append(random.randint(97, 122))
  return ''.join(map(chr, string_as_int_array))

def generate_random_value():
  return random.randint(1, 1000)

def random_element():
  return Element(generate_random_key(), generate_random_value())

def hash_table_test():
  # Create hash table
  h = HashTable()

  # Populate it
  for _ in range(100):
    h.add(random_element())
  h.add(Element('topher', 1337))

  # Print the table
  h.print()

  # Try a find
  print(h.find('topher').output())

def tree_test():
  # Create a tree
  my_tree = tree.Tree()

  # Populate it
  [my_tree.add(random_element()) for _ in range(10)]
  my_tree.add(Element('topher', 1349))

def tree_timeit():
  t = timeit.Timer("tree_test()", "from tester import tree_test")
  print(min(t.repeat(number=1000,repeat=3)))
  

def main():
  tree_timeit()

if __name__ == '__main__':
  main()
