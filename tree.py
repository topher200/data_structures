#!/usr/bin/python3

from element import Element

class Tree():
  def __init__(self):
    self.root = None

  def add(self, element):
    if self.root == None:
      self.root = Leaf(element)
    else:
      Tree._recursive_add(self.root, element)

  # pprint stands for pretty print- outputs root and all children
  def pprint(self):
    self._recursive_print(self.root)
    
  @staticmethod
  def _recursive_add(parent, element):
    if (element.key <= parent.element.key):
      if (parent.left_child == None):
        parent.left_child = Leaf(element)
      else:
        Tree._recursive_add(parent.left_child, element)
    else:
      if (parent.right_child == None):
        parent.right_child = Leaf(element)
      else:
        Tree._recursive_add(parent.right_child, element)

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
