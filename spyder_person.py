# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:52:22 2021

@author: Keisha
"""

class Person:
    def __init__(self,the_name,the_sex,the_age):
        self.name = the_name
        self.sex = the_sex
        self.age = the_age
    
person1 = Person("Chidalu","male",20)
person2 = Person("Bola","female",12)
print(person1.age)