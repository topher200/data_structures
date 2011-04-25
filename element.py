#!/usr/bin/python3

class Element():
  def __init__(self, key, value):
    self.key = key
    self.value = value

  def output(self):
    return('[{0} {1}]'.format(self.key, self.value))
