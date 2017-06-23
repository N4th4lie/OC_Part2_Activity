# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:36:16 2017

@author: user N4th4lie
"""

# Nombre de "bob" dans un mot

n = len(s)
bob = 0
for i in range(n-2):
    test=""
    for j in range(3):
        test+=s[i+j]                
    if test=="bob":
        bob+=1
print("Number of times bob occurs is:",bob)