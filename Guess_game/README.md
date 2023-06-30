<h1 align="center">Exercise: Guess my Number</h1>

<br>

In this problem, I created a program that guesses a secret number!

**The program works as follows**: You (the user) thinks of an integer between `0` (inclusive) and `100` (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:

    Please think of a number between 0 and 100!
    Is your secret number 50?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
    Is your secret number 75?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
    Is your secret number 87?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
    Is your secret number 81?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
    Is your secret number 84?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
    Is your secret number 82?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
    Is your secret number 83?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
    Game over. Your secret number was: 83

<br>

When the user enters something invalid, the computer should print out a message to the user explaining you did not understand their input. Then, it should re-ask the question, and prompt again for input. For example:

    Is your secret number 91?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
    Sorry, I did not understand your input.
    Is your secret number 91?
    Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c

### Solution

<hr>

[Guess Game Code](Guesses.py)

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
