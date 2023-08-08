# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:17:19 2023

@author: vtondlekar
Write a function that stutters a word as if someone is
struggling to read it. The first two letters are repeated
twice with an ellipsis ... and space after each, and then
the word is pronounced with a question mark ?.

Assume all input is in lower case and at least two
characters long.
stutter("incredible") ➞ "in... in... incredible?"
"""

def stutter(word):
    return word[:2] + '... ' + word[:2]+ '... ' + word + '?'
