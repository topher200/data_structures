#!/usr/bin/python3

from element import Element

class Tree():
  def __init__(self):
    self.root = None

  def add(self, element):
    self.root = Tree._recursive_add(self.root, element)

  def find(self, key):
    return Tree._recursive_find(self.root, key)

  # outputs root and all children
  def print(self):
    self._recursive_print(self.root)
    
  @staticmethod
  def _recursive_add(parent, element):
    if parent == None:
      return Leaf(element)

    if (element.key <= parent.element.key):
      parent.left_child = Tree._recursive_add(parent.left_child, element)
    else:
      parent.right_child = Tree._recursive_add(parent.right_child, element)
    return parent

  @staticmethod
  def _recursive_find(parent, key):
    # Check the current element (parent)
    if (parent == None):
      return None
    if (parent.element.key == key):
      return parent.element

    # Recursively try the children
    left_element = Tree._recursive_find(parent.left_child, key)
    if (left_element != None):
      return left_element
    right_element = Tree._recursive_find(parent.right_child, key)
    if (right_element != None):
      return right_element


  @staticmethod
  def _recursive_print(parent):
    if (parent == None):
      print()
      return(None)
    print('L:', end='')
    Tree._recursive_print(parent.left_child)
    print('M:{0}'.format(parent.element.output()))
    print('R:', end='')
    Tree._recursive_print(parent.right_child)


class Leaf():
  def __init__(self, element):
    self.element = element
    self.left_child = None
    self.right_child = None
