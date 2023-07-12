# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 14:28:12 2023

@author: Cristian David Polo Garrido
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    valid = False
    hand_copy = hand.copy()
    acum = 0

    if(word in wordList):
        for letter in word:
            if(hand_copy.get(letter,0)) != 0:
                acum += 1
                hand_copy[letter] -= 1
        if(acum == len(word)):
            valid = True
    
    return valid