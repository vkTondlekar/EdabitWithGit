# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:44:21 2023

@author: vtondlekar
Create a function that takes two arguments: the original
price and the discount percentage as integers and returns
the final price after the discount.

Notes
Your answer should be rounded to two decimal places.
"""

def dis(price, discount):
    return round ((price-((price*discount)/100)), 2)
