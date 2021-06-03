# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:33:02 2021

@author: Keisha
"""

class Student:
    name = 'Student'
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    @classmethod
    def info(cls):
        return cls.name

print(Student.info())

print("There are 2 instance variables, 1 class method, 1 class variable, and no instance method")
