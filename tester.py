#!/usr/bin/python3

import random
from element import Element
from hash_table import HashTable
import tree

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
  root = tree.Leaf(Element('topher', 1337))

  [tree.add(root, random_element()) for _ in range(10)]
  tree.add(root, Element('asdf', 239))

  tree.my_print(root)
  

def main():
  tree_test()

if __name__ == '__main__':
  main()
