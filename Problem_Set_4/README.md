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

If you choose the second case (let the computer play for you). In this part, you will be able to compare how you as a user succeed in the game compared to the computer's performance.

You should look at the following two functions: `compChooseWord` and `compPlayHand`, before entering to see the whole code.

<hr>

### compChooseWord

<br>

In this function, you'll see that the code creates a computer player that is legal, but not always the best. Try to walk through and understand the implementation.

**A Note On Runtime**: You may notice that things run a bit slowly when the computer plays. This is to be expected - the `wordList` has 83667 words, after all! 
