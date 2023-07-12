# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 18:25:28 2023

@author: Cristian David Polo Garrido
"""

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    
    values = []
    cont = 0

    for val in hand.values():
        values.append(val)
    
    for num in values:
        cont += num
    
    return cont