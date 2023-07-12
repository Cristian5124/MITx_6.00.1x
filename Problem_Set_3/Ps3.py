# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:21:43 2023

@author: Cristian David Polo Garrido
"""

# Hangman game

import random

WORDLIST_FILENAME = "Problem_Set_3\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    ''' 
    lettersGuessed = input()
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
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    This is an interactive game of Hangman.

    * At the start of the game, the game let the user know how many 
      letters the secretWord contains.

    * The gamme asks the user to supply one guess (i.e. letter) per round.

    * The user receives feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, the game also displays to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    '''
    print('Welcome to the game Hangman!')
    long = len(secretWord)
    print('I am thinking of a word that is '+str(long)+' letters long.')
    cont = 8
    lettersGuessed = []
    letra_usuario = ''
    letrasingresadas = ['']
    cont2=8

    while(cont>=0):
        print('-------------')
        print('You have '+str(cont)+' guesses left.')

        if(cont2==8):
            letras = getAvailableLetters(lettersGuessed)
            letrasdisp = []
            for x in letras:
                letrasdisp.append(x)

        if(letra_usuario!='' and letra_usuario in letrasdisp):
            letrasdisp.remove(letra_usuario)
        
        ans=''
        for x in letrasdisp:
            ans+=x

        print('Available letters: '+ans)

        letra_usuario = input('Please guess a letter: ')
        letra_usuario = letra_usuario.lower()

        letrasingresadas.append(letra_usuario)
        
        if(letra_usuario in secretWord):
            lettersGuessed.append(letra_usuario)

        impresion = getGuessedWord(secretWord, lettersGuessed)
        if('' in letrasingresadas):
            letrasingresadas.remove('')

        if(letra_usuario in letrasingresadas and letrasingresadas.count(letra_usuario)>1):
            print("Oops! You've already guessed that letter: "+impresion)
        
        elif(letra_usuario not in secretWord):
            print('Oops! That letter is not in my word: '+impresion)
            cont-=1       
        
        elif(letra_usuario in secretWord):
            print('Good guess: '+impresion)

        if(impresion==secretWord):
            print('------------')
            print('Congratulations, you won!')
            break
        if(cont==0):
            print('------------')
            print('Sorry, you ran out of guesses. The word was',secretWord+'.')
            break
        
        cont2-=1

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)