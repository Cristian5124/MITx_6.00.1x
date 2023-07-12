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
        displayHand(hand_copy)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        
        if word == '.':
            print('Goodbye! Total score:', score, 'points.')
            print()
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
    
        num_letters = calculateHandlen(hand_copy)
        
        if(num_letters == 0):
            print('Run out of letters. Total score:', score, 'points.')
            print()

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

def main():
    wordList = loadWords()
    playGame(wordList)
main()