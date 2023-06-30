# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 12:18:02 2023

@author: Cristian David Polo Garrido
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ans = []
    for letter in secretWord:
        ans.append("_")

    cont=0

    for letra in secretWord:
        if letra in lettersGuessed:
            ans.pop(cont)
            ans.insert(cont, letra)
        cont+=1

    string=''
    for elemento in ans:
        string+=elemento
        if elemento == '_':
            string+=' '
    return string
