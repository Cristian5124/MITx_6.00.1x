# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 14:46:34 2023

@author: Cristian David Polo Garrido
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    hand_copy = hand.copy()
    for letter in word:
        hand_copy[letter] -= 1
    return hand_copy