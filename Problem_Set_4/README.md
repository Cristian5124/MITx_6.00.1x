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

If you are a Windows user, you will have to change the backslashes to forward slashes.
