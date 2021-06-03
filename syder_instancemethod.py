# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 11:16:33 2021

@author: Keisha
"""

class Student:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def avg(self):
        return (self.a + self.b)/2
    
s1 = Student(10,20)
print( s1.avg())