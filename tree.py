#!/usr/bin/python3

from element import Element

def add(root, element):
  if (root == None):
    return element

  if (element.key <= root.element.key):
    if (root.left_child == None):
      root.left_child = Leaf(element)
    else:
      add(root.left_child, element)
  else:
    if (root.right_child == None):
      root.right_child = Leaf(element)
    else:
      add(root.right_child, element)

def my_print(root):
  if (root == None):
    print()
    return(None)
  print('L:', end='')
  my_print(root.left_child)
  print('M:{0}'.format(root.element.output()))
  print('R:', end='')
  my_print(root.right_child)

        
class Leaf():
  def __init__(self, element):
    self.element = element
    self.left_child = None
    self.right_child = None
