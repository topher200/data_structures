import random
from hash_table import HashTable, Element

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

def main():
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

if __name__ == '__main__':
  main()
