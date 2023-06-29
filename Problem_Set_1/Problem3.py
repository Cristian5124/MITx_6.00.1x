# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:40:43 2023

@author: Cristian David Polo Garrido
"""

def substring(s):
    min = 0
    substring = []
    for i in range(len(s)):
        cont = 0
        for j in range(i+1,len(s)):
            if ord(s[i+cont]) <= ord(s[j]):
                cont += 1
            else:
                break
        cont += 1
        min = max(cont,min)
        substring.append(cont)
        
    for i in range(len(substring)):
        if substring[i] == min:
            print(s[i:i+substring[i]])
            break