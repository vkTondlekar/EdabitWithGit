# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 19:56:19 2023

@author: vtondlekar

When resistors are connected together in series, the same current passes
through each resistor in the chain and the total resistance, RT, of the
circuit must be equal to the sum of all the individual resistors added
together. That is:

RT = R1 + R2 + R3 ...
Create a function that takes an array of values resistance that are connected
 in series, and calculates the total resistance of the circuit in ohms.
 The ohm is the standard unit of electrical resistance in the International
 System of Units ( SI ).

 series_resistance([1, 5, 6, 3]) ➞ "15 ohms"

 Notes
All inputs will be valid.
Notice the singular ohm for values <= 1.

"""

def series_resistance(r1, r2, r3, r4):
    r_total = (r1+r2+r3+r4)
    return(f"Total series resistance is {r_total} ohm")
