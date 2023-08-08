# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:50:16 2023

@author: vtondlekar
Create a function that finds the maximum range of a triangle's
 third edge, where the side lengths are all integers.

"""

def next_edge(side1,side2):
    return((side1+side2-1))


def minlength(side1,side2):
    return((max(side1,side2)- min(side1,side2))+1)
