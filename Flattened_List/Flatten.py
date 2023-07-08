# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 10:47:21 2023

@author: Cristian David Polo Garrido
"""

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    
    lista = []
    
    for element in aList:
        if type(element) == list:
            lista += flatten(element)
        else:
            lista.append(element)
    return lista

aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]   # Here can be any list
print(flatten(aList))