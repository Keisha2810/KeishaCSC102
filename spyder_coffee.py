# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:25:41 2021

@author: Keisha
"""

class Coffee:
    coffeeCupCounter = 0  # initialize class variable 
    def __init__(self, themilk, thesugar, thecoffeemate):
        self.milk  = themilk  # initialize intance variable 
        self.sugar = thesugar  # initialize intance variable 
        self.coffeemate = thecoffeemate  # initialize intance variable 
        Coffee.coffeeCupCounter= Coffee.coffeeCupCounter +1
        print(f"you now have your coffee with {self.milk} milk, {self.sugar} sugar and {self.sugar} coffeemate")
        

mySugarFreeCoffee = Coffee(2,-200,1)  # instantiation - object creation
print(mySugarFreeCoffee.sugar)
myMuchSugarCoffee = Coffee(2,10,1)
print(myMuchSugarCoffee.sugar)  # instantiation or object creation
print(f"we have made {Coffee.coffeeCupCounter} coffee cups so far!")
Coffee.coffeeCupCounter = 300 
print(f"we have made {mySugarFreeCoffee.coffeeCupCounter} coffee cups so far!")
print(f"we have made {myMuchSugarCoffee.milk} coffee cups so far!")
print(f"we have made {myMuchSugarCoffee.coffeeCupCounter} coffee cups so far!")