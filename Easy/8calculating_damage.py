# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:21:10 2023

@author: vtondlekar

Create a function that takes damage and speed (attacks per second)
and returns the amount of damage after a given time.

Notes
Return "invalid" if damage or speed is negative.
"""
#Dictionary-key:value pairs - {} used
thisdict ={'second':1, 'minute':60, 'hour':3600}
#print(type(thisdict))

def damage(damage, speed, time):
    if speed < 0 or damage < 0:
        return("Invalid input, non negative input please")
    else:
        return(damage * speed * thisdict.get(time))

