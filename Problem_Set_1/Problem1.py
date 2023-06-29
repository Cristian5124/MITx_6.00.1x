# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 12:32:18 2023

@author: Cristian David Polo Garrido
"""

def vowels(s):
    vowels=0
    for x in s:
        if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
            vowels+=1
    print('Number of vowels: '+str(vowels))