# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 11:27:43 2023

@author: Cristian David Polo Garrido
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    lista = []
    for x in secretWord:
        lista.append(x)

    for x in lista:
        while(lista.count(x)>1):
            lista.remove(x)
    
    cont=0
    for letter in lista:
        if letter in lettersGuessed:
            cont+=1
    
    if cont==len(lista):
        return True
    else:
        return False
                