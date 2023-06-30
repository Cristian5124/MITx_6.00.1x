# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 16:34:51 2023

@author: Cristian David Polo Garrido
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    letras = []
    a = string.ascii_lowercase
    for letter in a:
        letras.append(letter)
    for x in lettersGuessed:
        letras.remove(x)
    ans = ''
    for y in letras:
        ans+=y
    return ans