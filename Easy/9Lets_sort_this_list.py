# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:46:20 2023

@author: vtondlekar

Create a function that takes a list of numbers lst, a string s and
return a list of numbers as per the following rules:
    "Asc" returns a sorted list in ascending order.
    "Des" returns a sorted list in descending order.
    "None" returns a list without any modification.

    asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]
    asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]
    asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]

"""
#List items are ordered, changeable, and allow duplicate values
#items can be of any data type

def asc_des_none(lst, s):
    if s == "Des":
        return sorted(lst, reverse=True)
    if s == "Asc":
        return sorted(lst, reverse=False)
    if s == "None":
        return lst


