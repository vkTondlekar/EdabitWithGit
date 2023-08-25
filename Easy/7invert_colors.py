# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 13:03:33 2023

@author: vtondlekar

Create a function that inverts the rgb values of a given tuple.

Notes
Must return a tuple.
255 is the max value of a single color channel.
"""

def color_invert(r=int(),g=int(),b=int()):
    result = []
    #print (result)
    for i in r,g,b:
        result.append(255-i)
        #print(result)
    return tuple(result)
