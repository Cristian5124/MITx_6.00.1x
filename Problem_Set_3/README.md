<h1 align="center">Problem Set 3</h1>

### Introduction

<hr>

For this problem, I will implement a variation of the classic wordgame Hangman. For those of you who are unfamiliar with the rules, you may read all about it [here](http://en.wikipedia.org/wiki/Hangman%20%28game%29). In this problem, the second player will always be the computer, who will be picking a word at random.

<br>

In this problem, I will implement a function, called hangman, that will start up and carry out an interactive Hangman game between a player and the computer. Before we get to this function, we'll first implement a few helper functions to make it more easy.

<br>

For this problem, you will need the code files [Ps3.py](Ps3.py) and [words.txt](words.txt). Click on each and download them. Be sure to save them in same directory. Open and run the file *Ps3.py* without making any modifications to it, in order to ensure that everything is set up correctly. By "open and run" I mean do the following:

  * Go to your IDE. From the File menu, choose "Open".
  * Find the file `Ps3.py` and choose it.
  * The template `Ps3.py` file should now be open. Run the file.

<br>

The code I have given you loads in a list of words from a file. If everything is working okay, after a small delay, you should see the following printed out:

    Loading word list from file...
    55909 words loaded.

<br>

If you see an IOError instead (e.g., "No such file or directory"), you should change the value of the WORDLIST_FILENAME constant (defined near the top of the file) to the complete pathname for the file words.txt (This will vary based on where you saved the file). Windows users, change the backslashes to forward slashes, like below.

<br>

For example, if you saved `Ps3.py` and `words.txt` in the directory "C:/Users/Kevin/" change the line:

WORDLIST_FILENAME = "words.txt"  to something like
  
WORDLIST_FILENAME = "C:/Users/Kevin/words.txt"

<br>

**This folder will vary depending on where you saved the files.**

<hr>

### **Sample Output**

**The output of a winning game should look like this...**

        Loading word list from file...
        55900 words loaded.
        Welcome to the game, Hangman!
        I am thinking of a word that is 4 letters long.
        -------------
        You have 8 guesses left.
        Available letters: abcdefghijklmnopqrstuvwxyz
        Please guess a letter: a
        Good guess: _ a_ _
        ------------
        You have 8 guesses left.
        Available letters: bcdefghijklmnopqrstuvwxyz
        Please guess a letter: a
        Oops! You've already guessed that letter: _ a_ _
        ------------
        You have 8 guesses left.
        Available letters: bcdefghijklmnopqrstuvwxyz
        Please guess a letter: s
        Oops! That letter is not in my word: _ a_ _
        ------------
        You have 7 guesses left.
        Available letters: bcdefghijklmnopqrtuvwxyz
        Please guess a letter: t
        Good guess: ta_ t
        ------------
        You have 7 guesses left.
        Available letters: bcdefghijklmnopqruvwxyz
        Please guess a letter: r
        Oops! That letter is not in my word: ta_ t
        ------------
        You have 6 guesses left.
        Available letters: bcdefghijklmnopquvwxyz
        Please guess a letter: m
        Oops! That letter is not in my word: ta_ t
        ------------
        You have 5 guesses left.
        Available letters: bcdefghijklnopquvwxyz
        Please guess a letter: c
        Good guess: tact
        ------------
        Congratulations, you won!

<br>

**And the output of a losing game should look like this...**

        Loading word list from file...
        55900 words loaded.
        Welcome to the game Hangman!
        I am thinking of a word that is 4 letters long
        -----------
        You have 8 guesses left
        Available Letters: abcdefghijklmnopqrstuvwxyz
        Please guess a letter: a
        Oops! That letter is not in my word: _ _ _ _
        -----------
        You have 7 guesses left
        Available Letters: bcdefghijklmnopqrstuvwxyz
        Please guess a letter: b
        Oops! That letter is not in my word: _ _ _ _
        -----------
        You have 6 guesses left
        Available Letters: cdefghijklmnopqrstuvwxyz
        Please guess a letter: c
        Oops! That letter is not in my word: _ _ _ _
        -----------
        You have 5 guesses left
        Available Letters: defghijklmnopqrstuvwxyz
        Please guess a letter: d
        Oops! That letter is not in my word: _ _ _ _
        -----------
        You have 4 guesses left
        Available Letters: efghijklmnopqrstuvwxyz
        Please guess a letter: e
        Good guess: e_ _ e
        -----------
        You have 4 guesses left
        Available Letters: fghijklmnopqrstuvwxyz
        Please guess a letter: f
        Oops! That letter is not in my word: e_ _ e
        -----------
        You have 3 guesses left
        Available Letters: ghijklmnopqrstuvwxyz
        Please guess a letter: g
        Oops! That letter is not in my word: e_ _ e
        -----------
        You have 2 guesses left
        Available Letters: hijklmnopqrstuvwxyz
        Please guess a letter: h
        Oops! That letter is not in my word: e_ _ e
        -----------
        You have 1 guesses left
        Available Letters: ijklmnopqrstuvwxyz
        Please guess a letter: i
        Oops! That letter is not in my word: e_ _ e
        -----------
        Sorry, you ran out of guesses. The word was else.

### Problem 1 - Is the Word Guessed

<hr>

Please read the Hangman Introduction before starting reading this problem. I'll start by writing 3 simple functions that will help us easily code the Hangman problem. First, I implemented the function `isWordGuessed` that takes in two parameters - a string, `secretWord`, and a list of letters, `lettersGuessed`. This function returns a boolean - `True` if `secretWord` has been guessed (ie, all the letters of `secretWord` are in `lettersGuessed`) and `False` otherwise.

<br>

Example Usage:

    >>> secretWord = 'apple' 
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(isWordGuessed(secretWord, lettersGuessed))
    False

For this function, **all** the letters in secretWord and lettersGuessed are lowercase.

### Solution

<hr>

[Problem 1](Problem7.py)

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
                

<br>

### Problem 2 - Getting the User's Guess

<hr>

Next, I will implement the function `getGuessedWord` that takes in two parameters - a string, `secretWord`, and a list of letters, `lettersGuessed`. This function returns a string that is comprised of letters and underscores, based on what letters in `lettersGuessed` are in `secretWord`. This is not too different from `isWordGuessed`!

<br>

Example Usage:

    >>> secretWord = 'apple' 
    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(getGuessedWord(secretWord, lettersGuessed))
    '_ pp_ e'

For this function, **all** the letters in secretWord and lettersGuessed are lowercase.

### Solution

<hr>

[Problem 2](Problem8.py)

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
  
<br>

### Problem 3 - Printing Out all Available Letters

<hr>

Next, I implemented the function `getAvailableLetters` that takes in one parameter - a list of letters, `lettersGuessed`. This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are **not** in `lettersGuessed`.

<br>

Example Usage:

    >>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    >>> print(getAvailableLetters(lettersGuessed))
    abcdfghjlmnoqtuvwxyz
    
> Note that this function should return the letters in alphabetical order, as in the example above.

For this function, **all** the letters in secretWord and lettersGuessed are lowercase.

### Solution

<hr>

[Problem 3](Problem9.py)

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

<br>

### Problem 4 - The Game

<hr>

Now I will implement the function `hangman`, which takes one parameter - the `secretWord` the user is to guess. This starts up an interactive game of Hangman between the user and the computer. In this function, I took advantage of the three helper functions, `isWordGuessed`, `getGuessedWord`, and `getAvailableLetters`, that I've defined in the previous part.

<br>

There are four important pieces of information I stored in this function:
  1. `secretWord`: The word to guess.
  2. `lettersGuessed`: The letters that have been guessed so far.
  3. `mistakesMade`: The number of incorrect guesses made so far.
  4. `availableLetters`: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter is removed from `availableLetters` (and if they guess a letter that is **not** in `availableLetters`, the program should print a message telling them they've already guessed that - so try again!).

### Solution

<hr>

[Problem 4](Ps3.py)

    # -*- coding: utf-8 -*-
    """
    Created on Tue Jun 27 14:21:43 2023
    
    @author: Cristian David Polo Garrido
    """
    
    # Hangman game
    
    import random
    
    WORDLIST_FILENAME = "Downloads\words.txt"
    
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
