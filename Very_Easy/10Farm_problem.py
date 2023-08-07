# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:46:46 2023

@author: vtondlekar
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you
a subtotal for each species. You have to implement
a function that returns the total number of legs of
all the animals.
"""

def animals(chickens, cows, pigs):
    return int ((chickens*2)+(cows*4)+(pigs*4))
