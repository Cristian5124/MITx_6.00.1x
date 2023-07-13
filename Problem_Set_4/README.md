<h1 align="center">Problem Set 4</h1>

### Introduction

<hr>

In this problem set, I'll implement a version of a wordgame! <br><br>
Let's begin by describing the __6.00 wordgame__: This game is a lot like Scrabble or Words With Friends, if you've played those. <br> Letters are dealt to players, who then construct one or more words out of their letters. Each **valid** word receives a score, based on the length of the word and the letters in that word.

The rules of the game are as follows: <br> <br>

**Dealing** <br> <br>
  * A player is dealt a hand of `n` letters chosen at random (*n=7* for now). <br> <br>
  * The player arranges the hand into as many words as they want out of the letters, using each letter at most once. <br> <br>
  * Some letters may remain unused (these won't be scored). <br> <br>

<a name='scoring'></a>
**Scoring** <br> <br>
  * The score for the hand is the sum of the scores for each word formed. <br> <br>
  * The score for a word is the sum of the points for letters in the word, multiplied by the length of the word, plus 50 points if all `n` letters are used on the first word created. <br> <br>
  * Letters are scored as in Scrabble; **A** is worth 1, **B** is worth 3, **C** is worth 3, **D** is worth 2, **E** is worth 1, and so on. I have defined the dictionary SCRABBLE_LETTER_VALUES that maps each lowercase letter to its Scrabble letter value. <br> <br>
  * For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, then multiply by len('weed') to get (4+1+1+2)*4 = 32). The program should check that the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word! <br> <br>
  * As another example, if *n=7* and you make the word 'waybill' on the first try, it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, plus an additional 50 point bonus for using all `n` letters). <br> <br>

### **Sample Output**

**Here is how the game output will look!**

    Loading word list from file...
       83667 words loaded.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: p z u t t t o
    Enter word, or a "." to indicate that you are finished: tot
    "tot" earned 9 points. Total: 9 points
    Current Hand: p z u t
    Enter word, or a "." to indicate that you are finished: .
    Total score: 9 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Current Hand: p z u t t t o
    Enter word, or a "." to indicate that you are finished: top
    "top" earned 15 points. Total: 15 points
    Current Hand: z u t t
    Enter word, or a "." to indicate that you are finished: tu
    Invalid word, please try again.
    Current Hand: z u t t
    Enter word, or a "." to indicate that you are finished: .
    Total score: 15 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: a q w f f i p
    Enter word, or a "." to indicate that you are finished: paw
    "paw" earned 24 points. Total: 24 points
    Current Hand: q f f i
    Enter word, or a "." to indicate that you are finished: qi
    "qi" earned 22 points. Total: 46 points
    Current Hand: f f
    Enter word, or a "." to indicate that you are finished: .
    Total score: 46 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: a r e t i i n
    Enter word, or a "." to indicate that you are finished: inertia
    "inertia" earned 99 points. Total: 99 points
    Run out of letters. Total score: 99 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

<br>

### Getting Started

<hr>

1. Download and save [Problem Set 4](https://github.com/Cristian5124/MITx_6.00.1x/releases/tag/Ps4), a zip file that contains the Problem Set code. Extract the files from the zip folder and make sure to save all the files `Ps4.py`, `Test_Ps4.py` and `words.txt` in the same folder. <br><br>
2. Run the file `Ps4.py`, without making any modifications to it, in order to ensure that everything is set up correctly (this means, open the file in IDLE, and use the Run command to load the file into the interpreter). The code I have given you loads a list of valid words from a file and then calls the *playGame* function. If everything is okay, after a small delay, you should see the following printed out:

       Loading word list from file...
          83667 words loaded.
       Enter n to deal a new hand, r to replay the last hand, or e to end game: 

If you see an IOError instead (e.g., "No such file or directory"), you should change the value of the *WORDLIST_FILENAME* constant (defined near the top of the file) to the **complete pathname** for the file `words.txt` (This will vary based on where you saved the files).

For example, if you saved all the files including this `words.txt` in the directory "C:/Users/Ana/Downloads" change the line: 

WORDLIST_FILENAME = "words.txt"  to something like <br>
WORDLIST_FILENAME = "C:/Users/Ana/Downloads/words.txt" or "Downloads/words.txt"

If you are a Windows user, you will have to change the backslashes to forward slashes. <br><br>

3. This problem set is structured so there are some modular functions that work together to form the complete word playing game. To be sure that those functions work correctly, open the `Test_Ps4.py` code and test each function, individually, before moving on. This approach is known as *unit testing*, and it was helpful to debug the code.

If the code passes the unit tests you will see a **SUCCESS message**; otherwise you will see a **FAILURE message**. These tests aren't exhaustive. You will want to test the game with your own parameters.

Try running `Test_Ps4.py` now. You should see that all tests pass, but you can try modifying some values to see if it works for all cases.

These are the provided test functions:

test_getWordScore()
     
>   Tests the getWordScore() implementation.
     
test_updateHand()
    
>   Tests the updateHand() implementation.

test_isValidWord()

>   Tests the isValidWord() implementation.

<br>

### Problem 1 - Word Scores

<hr>

The first step is to implement some code that allows us to calculate the score for a single word. The function `getWordScore` should accept as input a string of lowercase letters (*a word*) and return the integer score for that word, using the [game's scoring rules](#scoring).

### Solution

<hr>

[Problem 1](Problem10.py)

    # -*- coding: utf-8 -*-
    """
    Created on Thu Jul 06 14:28:12 2023
    
    @author: Cristian David Polo Garrido
    """

    def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
    
    score *= len(word)

    if len(word) == n:
        score += 50

    return score                

<br>

### Problem 2 - Dealing with Hands

<hr>

### Representing Hands

<br>

A **hand** is the set of letters held by a player during the game. The player is initially dealt a set of random letters. For example, the player could start out with the following hand: `a, q, l, m, u, i, l`. In this program, a hand will be represented as a dictionary: The keys are (lowercase) letters and the values are the number of times the particular letter is repeated in that hand. For example, the above hand would be represented as:

    hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}

Notice how the repeated letter `'l'` is represented. Remember that with a dictionary, the usual way to access a value is `hand['a']`, where `'a'` is the key we want to find. However, this only works if the key is in the dictionary; otherwise, we get a `KeyError`. To avoid this, we can use the call `hand.get('a',0)`. This is the "safe" way to access a value if we are not sure the key is in the dictionary. `hand.get(key,default)` returns the value for `key` if `key` is in the dictionary `hand`, else `default`. If `default` is not given, it returns `None`, so that this method never raises a `KeyError`. For example:

    >>> hand['e']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'e'
    >>> hand.get('e', 0)
    0

<hr>

### Converting Words Into Dictionary Representation

<br>

One useful function I've defined is `getFrequencyDict`, defined near the top of `Ps4.py`. When given a string of letters as an input, it returns a dictionary where the keys are letters and the values are the number of times that letter is represented in the input string. For example:

    >>> getFrequencyDict("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}

As you can see, this is the same kind of dictionary I use to represent hands.

<hr>

### Displaying a Hand

<br>

Given a hand represented as a dictionary, we want to display it in a user-friendly way. I have provided the implementation for this in the `displayHand` function. Take a few minutes to read through this function carefully and understand what it does and how it works.

<hr>

### Generating a Random Hand

<br>

The hand a player is dealt is a set of letters chosen at random. The function `dealHand` generates this random hand. The function takes as input a positive integer `n`, and returns a new object, a hand containing `n` lowercase letters. Again, take a few minutes to read through this function carefully and understand what it does and how it works.

<hr>

### Removing Letters From a Hand

<br>

The player starts with a hand, a set of letters. As the player spells out words, letters from this set are used up. For example, the player could start out with the following hand: `a, q, l, m, u, i, l`. The player could choose to spell the word `quail`. This would leave the following letters in the player's hand: `l, m`. The task is to implement the function `updateHand`, which takes in two inputs - a `hand` and a `word` (string). `updateHand` uses letters from the hand to spell the word, and then returns a copy of the `hand`, containing only the letters remaining. For example:

    >>> hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    >>> displayHand(hand) # Implemented for you
    a q l l m u i
    >>> hand = updateHand(hand, 'quail') # You implement this function!
    >>> hand
    {'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}
    >>> displayHand(hand)
    l m  

> It must not mutate the hand passed in.

### Solution

<hr>

[Problem 2](Problem11.py)    
    
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

<br>

### Problem 3 - Valid Words

<hr>

At this point, we have written code to generate a random hand and display that hand to the user. We can also ask the user for a word and score the word (using your `getWordScore`). However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game. A *valid* word is in the word list; **and** it is composed entirely of letters from the current hand.

### Solution

<hr>

[Problem 3](Problem12.py)

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

<br>        

### Problem 4 - Hand Length

<hr>

We are now ready to begin writing the code that interacts with the player. We'll be implementing the `playHand` function. This function allows the user to play out a single hand. First, though, we'll need to implement the helper `calculateHandlen` function, that returns the number of letters left in the hand.

### Solution

<hr>

[Problem 4](Problem13.py)

    # -*- coding: utf-8 -*-
    """
    Created on Thu Jul 06 18:25:28 2023
    
    @author: Cristian David Polo Garrido
    """
    
    def calculateHandlen(hand):
        """ 
        Returns the length (number of letters) in the current hand.
        
        hand: dictionary (string-> int)
        returns: integer
        """
        
        values = []
        cont = 0
    
        for val in hand.values():
            values.append(val)
        
        for num in values:
            cont += num
        
        return cont

<br>        

### Problem 5 - The Game

<hr>

### You and Your Computer

A game consists of playing multiple hands. We need to implement one final function to complete our word-game program. Read the code that implements the `playGame` function. In this function, you will see that there are two options, play a hand as a user or let the computer play. In the first case, we can play a new hand, replay the last hand or end the game by typing `'n'` for new, `'r'` for replay or `'e'` for end. When we start a new game, the program should print the current hand and as a user, you have to enter a word, or enter a single period `'.'`, the computer will print the score of the word and finally the total score.

<br>

### **Sample Output**

**Here is how the game output should look...**

    Loading word list from file...
       83667 words loaded.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    You have not played a hand yet. Please play a new hand first!
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: p z u t t t o
    Enter word, or a "." to indicate that you are finished: tot
    "tot" earned 9 points. Total: 9 points
    
    Current Hand: p z u t
    Enter word, or a "." to indicate that you are finished: .
    Goodbye! Total score: 9 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    Current Hand: p z u t t t o
    Enter word, or a "." to indicate that you are finished: top
    "top" earned 15 points. Total: 15 points
    
    Current Hand: z u t t
    Enter word, or a "." to indicate that you are finished: tu
    Invalid word, please try again.
    
    Current Hand: z u t t
    Enter word, or a "." to indicate that you are finished: .
    Goodbye! Total score: 15 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: a q w f f i p
    Enter word, or a "." to indicate that you are finished: paw
    "paw" earned 24 points. Total: 24 points
    
    Current Hand: q f f i
    Enter word, or a "." to indicate that you are finished: qi
    "qi" earned 22 points. Total: 46 points
    
    Current Hand: f f
    Enter word, or a "." to indicate that you are finished: .
    Goodbye! Total score: 46 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    Current Hand: a r e t i i n
    Enter word, or a "." to indicate that you are finished: inertia
    "inertia" earned 99 points. Total: 99 points.
    
    Run out of letters. Total score: 99 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: x
    Invalid command.
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

<br>

If you choose the second case, you are letting the computer play for you. In this part, you will be able to compare how you as a user succeed in the game compared to the computer's performance.

You should look at the following two functions: `compChooseWord` and `compPlayHand`, before entering to see the whole code.

<hr>

### compChooseWord

<br>

In this function, you'll see that the code creates a computer player that is legal, but not always the best. Try to walk through and understand the implementation.

**A Note On Runtime**: You may notice that things run a bit slowly when the computer plays. This is to be expected - the `wordList` has 83667 words, after all!

**Test Cases to Understand the Code:**

    >>> compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6) 
    appels 
    >>> compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5) 
    acta 
    >>> compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12) 
    immanent 
    >>> compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12) 
    None

<hr>

### compPlayHand

<br>

Now that we have the ability to let the computer choose a word, we need to set up a function to allow the computer to play a hand - in a manner very similar to the `playHand` function. This function allows the computer to play a given hand and is very similar to the earlier version in which a user selected the word, although deciding when it is done playing a particular hand is different.

**Test Cases to Understand the Code:**

    compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    Current Hand: a p p s e l
    "appels" earned 110 points. Total: 110 points
    Total score: 110 points.
    
    compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    Current Hand: a a c b t "acta" 
    earned 24 points. Total: 24 points 
    Current Hand: b Total score: 24 points. 
    
    compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    Current Hand: a a e e i i m m n n t t
    "immanent" earned 96 points. Total: 96 points
    Current Hand: a e t i
    "ait" earned 9 points. Total: 105 points
    Current Hand: e
    Total score: 105 points.

<hr>

At this point, the computer can choose a word if you give it the option to play. This code re-implements the `playGame` function and allows the user to choose between playing a game or letting the computer play.

<br>

### **Sample Output**

**Here is how the game output should look...**

    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    
    Enter u to have yourself play, c to have the computer play: u
    
    Current Hand: a s r e t t t
    Enter word, or a "." to indicate that you are finished: tatters
    "tatters" earned 99 points. Total: 99 points
    
    Run out of letters. Total score: 99 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    
    Enter u to have yourself play, c to have the computer play: c
    
    Current Hand:  a s r e t t t
    "stretta" earned 99 points. Total: 99 points
    
    Total score: 99 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: x
    Invalid command.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    
    Enter u to have yourself play, c to have the computer play: me
    Invalid command.
    
    Enter u to have yourself play, c to have the computer play: you
    Invalid command.
    
    Enter u to have yourself play, c to have the computer play: c
    
    Current Hand:  a c e d x l n
    "axled" earned 65 points. Total: 65 points
    
    Current Hand:  c n
    Total score: 65 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: n
    
    Enter u to have yourself play, c to have the computer play: u
    
    Current Hand: a p y h h z o
    Enter word, or a "." to indicate that you are finished: zap 
    "zap" earned 42 points. Total: 42 points
    
    Current Hand: y h h o
    Enter word, or a "." to indicate that you are finished: oy
    "oy" earned 10 points. Total: 52 points
    
    Current Hand: h h
    Enter word, or a "." to indicate that you are finished: .
    Goodbye! Total score: 52 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: r
    
    Enter u to have yourself play, c to have the computer play: c
    
    Current Hand:  a p y h h z o
    "hypha" earned 80 points. Total: 80 points
    
    Current Hand:  z o
    Total score: 80 points.
    
    Enter n to deal a new hand, r to replay the last hand, or e to end game: e

### Solution

<hr>

[Word Game](Ps4.py)

    # The 6.00 Word Game
    
    import random
    import string
    
    VOWELS = 'aeiou'
    CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
    HAND_SIZE = 7   #You can change this value in order to play different hand sizes.
    
    SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
                               'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
                                 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}
    
    # -----------------------------------
    
    WORDLIST_FILENAME = "Problem_Set_4\words.txt"
    
    def loadWords():
        """
        Returns a list of valid words. Words are strings of lowercase letters.
        
        Depending on the size of the word list, this function may
        take a while to finish.
        """
        
        print("Loading word list from file...")
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r')
        # wordList: list of strings
        wordList = []
        for line in inFile:
            wordList.append(line.strip().lower())
        print("  ", len(wordList), "words loaded.")
        return wordList
    
    # -----------------------------------
    
    def getFrequencyDict(sequence):
        """
        Returns a dictionary where the keys are elements of the sequence
        and the values are integer counts, for the number of times that
        an element is repeated in the sequence.
    
        sequence: string or list
        return: dictionary
        """
        
        # freqs: dictionary (element_type -> int)
        freq = {}
        for x in sequence:
            freq[x] = freq.get(x,0) + 1
        return freq
    	
    # -----------------------------------
    
    #
    # Problem #1: Scoring a word
    #
    def getWordScore(word, n):
        """
        Returns the score for a word. Assumes the word is a valid word.
    
        The score for a word is the sum of the points for letters in the
        word, multiplied by the length of the word, PLUS 50 points if all n
        letters are used on the first turn.
    
        Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
        worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
    
        word: string (lowercase letters)
        n: integer (HAND_SIZE; i.e., hand size required for additional points)
        returns: int >= 0
        """
        
        score = 0
        for letter in word:
            score += SCRABBLE_LETTER_VALUES[letter]
        
        score *= len(word)
    
        if len(word) == n:
            score += 50
    
        return score
    
    # -----------------------------------
    
    #
    # Problem #2: Display letters in a hand
    #
    def displayHand(hand):
        """
        Displays the letters currently in the hand.
    
        For example:
    
        >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
        Should print out something like:
           a x x l l l e
        The order of the letters is unimportant here because later I made a function that sorts the hand alphabetically.
    
        hand: dictionary (string -> int)
        """
        
        for letter in hand.keys():
            for j in range(hand[letter]):
                 print(letter,end=" ")       # print all on the same line
        print()                             # print an empty line
    
    # -----------------------------------
    
    #
    # Problem #2: Random hand
    #
    def dealHand(n):
        """
        Returns a random hand containing n lowercase letters.
        At least n/3 the letters in the hand should be VOWELS.
    
        Hands are represented as dictionaries. The keys are
        letters and the values are the number of times the
        particular letter is repeated in that hand.
    
        n: int >= 0
        returns: dictionary (string -> int)
        """
        
        hand={}
        numVowels = n // 3
        
        for i in range(numVowels):
            x = VOWELS[random.randrange(0,len(VOWELS))]
            hand[x] = hand.get(x, 0) + 1
            
        for i in range(numVowels, n):    
            x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
            hand[x] = hand.get(x, 0) + 1
            
        return hand
    
    # -----------------------------------
    
    #
    # Problem #2: Update a hand by removing letters
    #
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
    
    # -----------------------------------
    
    #
    # Function that sort alphabetically a hand
    #
    def sorthand(hand):
            """
            Returns the same hand but sorted alphabetically
            composed of letters in the hand. Otherwise, returns False.
    
            Does not mutate the elements of the hand, only it's order.
        
            hand: dictionary (string -> int)
            """
            
            sort_hand = {}
    
            for letter in SCRABBLE_LETTER_VALUES.keys():
                if hand.get(letter,0) != 0:
                    sort_hand[letter] = hand[letter]
            
            return sort_hand
    
    # -----------------------------------
    
    #
    # Problem #3: Test word validity
    #
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
    
    # -----------------------------------
    
    #
    # Problem #4: Playing a hand
    #
    
    def calculateHandlen(hand):
        """ 
        Returns the length (number of letters) in the current hand.
        
        hand: dictionary (string-> int)
        returns: integer
        """
        
        values = []
        cont = 0
    
        for val in hand.values():
            values.append(val)
        
        for num in values:
            cont += num
        
        return cont
    
    # -----------------------------------
    
    def playHand(hand, wordList, n):
        """
        Allows the user to play the given hand, as follows:
    
        * The hand is displayed.
        * The user may input a word or a single period (the string ".") 
          to indicate they're done playing
        * Invalid words are rejected, and a message is displayed asking
          the user to choose another word until they enter a valid word or "."
        * When a valid word is entered, it uses up letters from the hand.
        * After every valid word: the score for that word is displayed,
          the remaining letters in the hand are displayed, and the user
          is asked to input another word.
        * The sum of the word scores is displayed when the hand finishes.
        * The hand finishes when there are no more unused letters or the user
          inputs a "."
    
          hand: dictionary (string -> int)
          wordList: list of lowercase strings
          n: integer (HAND_SIZE; i.e., hand size required for additional points)
          
        """
        
        score = 0
        hand = sorthand(hand)
        hand_copy = hand.copy()
        num_letters = calculateHandlen(hand_copy)
    
        while(num_letters > 0):
            print('Current Hand: ', end='')
            displayHand(hand)
    
            chance = False
            
            # If the hand only has one letter left, ends the game
            if num_letters == 1: 
                print('No word of the word list is valid for this hand.')
                break
            
            # If there are vowels left or the letter 'y', there is a chance to find a valid word
            for letter in hand.keys():
                if (letter in ('a','e','i','o','u','y') and hand[letter] != 0):
                    chance = True
    
            # If there is no chance, ends the game
            if chance == False:
                print('No word of the word list is valid for this hand.')
                break
            
            else:
                word = input('Enter word, or a "." to indicate that you are finished: ')
                
                if word == '.':
                    print()
                    print('Goodbye! Total score:', score, 'points.')
                    break
                else:
                    valid = isValidWord(word, hand, wordList)
                    if valid == False:
                        print('Invalid word, please try again.')
                        print()
                    else:
                        word_score = getWordScore(word, n)
                        score += word_score
                        print('"'+str(word)+'"', 'earned', word_score, 'points. Total:', score, 'points')
                        print()
                        for letter in word:
                            hand_copy[letter] -= 1
                        hand = updateHand(hand,word)
                
                num_letters = calculateHandlen(hand_copy)
            
        if(num_letters == 0):
            print()
            print('Run out of letters. Total score:', score, 'points.')
    
        elif word != '.':
            print()
            print('Total score:',score, 'points.')
    
    # -----------------------------------
    
    #
    # Computer chooses a word
    #
    def compChooseWord(hand, wordList, n):
        """
        Given a hand and a wordList, find the word that gives 
        the maximum value score, and return it.
    
        This word should be calculated by considering all the words
        in the wordList.
    
        If no words in the wordList can be made from the hand, return None.
    
        hand: dictionary (string -> int)
        wordList: list (string)
        n: integer (HAND_SIZE; i.e., hand size required for additional points)
    
        returns: string or None
        """
        # Create a new variable to store the maximum score seen so far (initially 0)
        bestScore = 0
        # Create a new variable to store the best word seen so far (initially None)  
        bestWord = None
        # For each word in the wordList
        for word in wordList:
            valid = isValidWord(word, hand, wordList)
            # If you can construct the word from your hand
            if valid == True:
                # find out how much making that word is worth
                score = getWordScore(word, n)
                # If the score for that word is higher than your best score
                if (score > bestScore):
                    # update your best score, and best word accordingly
                    bestScore = score
                    bestWord = word
        # return the best word you found.
        return bestWord       
    
    # -----------------------------------
    
    #
    # Computer plays a hand
    #
    def compPlayHand(hand, wordList, n):
        """
        Allows the computer to play the given hand, following the same procedure
        as playHand, except instead of the user choosing a word, the computer 
        chooses it.
    
        1) The hand is displayed.
        2) The computer chooses a word.
        3) After every valid word: the word and the score for that word is 
        displayed, the remaining letters in the hand are displayed, and the 
        computer chooses another word.
        4)  The sum of the word scores is displayed when the hand finishes.
        5)  The hand finishes when the computer has exhausted its possible
        choices (i.e. compChooseWord returns None).
     
        hand: dictionary (string -> int)
        wordList: list (string)
        n: integer (HAND_SIZE; i.e., hand size required for additional points)
        """
        # Keep track of the total score
        score = 0
        # Number of letters left
        num_letters = calculateHandlen(hand)
        # As long as there are still letters left in the hand:
        while num_letters > 0:
            # Display the hand
            print('Current Hand: ', end='')
            displayHand(hand)
    
            chance = False
            
            # If the hand only has one letter left, ends the game
            if num_letters == 1: 
                print('No word of the word list is valid for this hand.')
                break
            
            # If there are vowels left or the letter 'y', there is a chance to find a valid word
            for letter in hand.keys():
                if (letter in ('a','e','i','o','u','y') and hand[letter] != 0):
                    chance = True
    
            # If there is no chance, ends the game
            if chance == False:
                print('No word of the word list is valid for this hand.')
                break
            
            else:
                # computer's word
                word = compChooseWord(hand, wordList, n)
                # If the input is a single period:
                if word == None:
                    print('No word of the word list is valid for this hand.')
                    # Ends the game (break out of the loop)
                    break
                    
                # Otherwise (the input is not a single period):
                else:
                    # See if the word is valid or not
                    valid = isValidWord(word, hand, wordList)
                    # If the word is not valid:
                    if valid == False:
                        print('No word of the word list is valid for this hand.')
                        break
                    # Otherwise (the word is valid):
                    else:
                        # Tells the user how many points the word earned, and the updated total score 
                        word_score = getWordScore(word, n)
                        score += word_score
                        print('"'+str(word)+'"', 'earned', word_score, 'points. Total:', score, 'points')             
                        # Updates hand and shows the updated hand to the user
                        hand = updateHand(hand, word)
                        print()
            
            num_letters = calculateHandlen(hand)
        # Game is over (user entered a '.' or ran out of letters), so tells user the total score
        print()
        print('Total score:',score, 'points.')
    
    # -----------------------------------
    
    #
    # Problem #5: Playing a game
    # 
    
    def playGame(wordList):
        """
        Allow the user to play an arbitrary number of hands.
     
        1) Asks the user to input 'n' or 'r' or 'e'.
            * If the user inputs 'e', immediately exit the game.
            * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.
    
        2) Asks the user to input a 'u' or a 'c'.
            * If the user inputs anything that's not 'c' or 'u', keep asking them again.
    
        3) Switch functionality based on the above choices:
            * If the user inputted 'n', play a new (random) hand.
            * Else, if the user inputted 'r', play the last hand again.
              But if no hand was played, output "You have not played a hand yet. 
              Please play a new hand first!"
            
            * If the user inputted 'u', let the user play the game
              with the selected hand, using playHand.
            * If the user inputted 'c', let the computer play the 
              game with the selected hand, using compPlayHand.
    
        4) After the computer or user has played the hand, repeat from step 1
    
        wordList: list (string)
        """
        
        game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        while (game not in ('n', 'e', 'r')):
            print('Invalid command.')
            game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        firstgame = False
        
        while (game!='e'):
            if game == 'n':
                print()
                ans = input('Enter u to have yourself play, c to have the computer play: ')
                while (ans not in ('u', 'c')):
                    print('Invalid command.')
                    print()
                    ans = input('Enter u to have yourself play, c to have the computer play: ')
                    
                if ans == 'u':
                    print()
                    n = HAND_SIZE
                    hand = dealHand(n)
                    hand = sorthand(hand)
                    playHand(hand, wordList, n)
                    print()
                    game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                    while (game not in ('n', 'e', 'r')):
                        print('Invalid command.')
                        game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                    firstgame = True
    
                else:
                    print()
                    n = HAND_SIZE
                    hand = dealHand(n)
                    hand = sorthand(hand)
                    compPlayHand(hand, wordList, n)
                    print()
                    game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                    while (game not in ('n', 'e', 'r')):
                        print('Invalid command.')
                        game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                    firstgame = True
            
            if game =='r':
                if firstgame == True:
                    print()
                    ans = input('Enter u to have yourself play, c to have the computer play: ')
                    while (ans not in ('u', 'c')):
                        print('Invalid command.')
                        print()
                        ans = input('Enter u to have yourself play, c to have the computer play: ')
                    
                    if ans == 'u':
                        print()
                        playHand(hand, wordList, n)
                        print()
                        game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                        while (game not in ('n', 'e', 'r')):
                            print('Invalid command.')
                            game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                    
                    else:
                        print()
                        compPlayHand(hand, wordList, n)
                        print()
                        game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                        while (game not in ('n', 'e', 'r')):
                            print('Invalid command.')
                            game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                
                else:
                    print('You have not played a hand yet. Please play a new hand first!')
                    print()
                    game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
                    while (game not in ('n', 'e', 'r')):
                        print('Invalid command.')
                        game = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
    
    # -----------------------------------
    
    if __name__ == '__main__':
        wordList = loadWords()
        playGame(wordList)
