# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:07:31 2023

@author: Cristian David Polo Garrido
"""

def guessgame(low = 0, high = 100):
    print(f'Please think of a number between {low} and {high}!')
    guess=int((low+high)/2)
    print(f'Is your secret number {guess}?')
    resp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    while (resp!='c'):

        if(resp!='h' and resp!='l'):
            print('Sorry, I did not understand your input.')
            print(f'Is your secret number {guess}?')
            resp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
        
        elif (resp=='l'):
            low=guess
            guess=int((low+high)/2)
            print(f'Is your secret number {guess}?')
            resp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

        else:
            high=guess
            guess=int((low+high)/2)
            print(f'Is your secret number {guess}?')
            resp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    print(f'Game over. Your secret number was: {guess}')