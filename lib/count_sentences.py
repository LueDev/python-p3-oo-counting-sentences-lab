#!/usr/bin/env python3
import re

class MyString:
  
  def __init__(self, value=""):
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, string):
    self._value=string if type(string) == str else print("The value must be a string.")
    
  
  def is_sentence(self):
    return True if self._value[-1] == "." else False

  def is_exclamation(self):
    return True if self._value[-1] == "!" else False
  
  def is_question(self):
    return True if self._value[-1] == "?" else False
  
  def count_sentences(self):
    results = re.split(r'[?.!]', self._value)
    return len([element for element in results if element])

if __name__ == "__main__":
  stringy = MyString("one. two. three?")
  # stringy = MyString(33)
  print(stringy.count_sentences())