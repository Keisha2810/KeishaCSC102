# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 14:23:16 2021

@author: Keisha
"""

from abc import ABC, abstractmethod
class Shape(ABC):
    def printx(self):
        print("I am a normal method defined inside the abstract class 'Shape'")
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Shape):
  length = 5
  breadth = 3
  def calculate_area(self):
    return self.length * self.breadth

rec = Rectangle()
rec.printx()
print("Area of a rectangle:", rec.calculate_area())