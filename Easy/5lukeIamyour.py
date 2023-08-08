# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 10:09:32 2023

@author: vtondlekar

Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

Person	Relation
Darth Vader	father
Leia	sister
Han	brother in law
R2D2	droid

relation_to_luke("Leia") ➞ "Luke, I am your sister."
"""
def relation_to_luke(name):
	if name == "Darth Vader":
		return "Luke, I am your father."
	if name == "Leia":
		return "Luke, I am your sister."
	if name == "Han":
		return "Luke, I am your brother in law."
	if name == "R2D2":
		return "Luke, I am your droid."
