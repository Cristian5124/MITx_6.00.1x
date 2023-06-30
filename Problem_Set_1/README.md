<h1 align="center">Problem Set 1</h1>

### Problem 1

<hr>

Assume `s` is a string of lower case characters. <br><br>
Write a program that counts up the number of vowels contained in the string `s`. Valid vowels are: '`a`', '`e`', '`i`', '`o`', and '`u`'. <br>
For example, if `s = 'azcbobobegghakl'`, your program should print: <br>

    Number of vowels: 5

### Solution

<hr>

[Problem 1](Problem1.py)

    # -*- coding: utf-8 -*-
    """
    Created on Wed Jun 21 12:32:18 2023
    
    @author: Cristian David Polo Garrido
    """
    
    def vowels(s):
        vowels=0
        for x in s:
            if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
                vowels+=1
        print('Number of vowels: '+str(vowels))

<br>

### Problem 2

<hr>

Assume `s` is a string of lower case characters. <br>

Write a program that prints the number of times the string `'bob'` occurs in `s`. <br>
For example, if `s = 'azcbobobegghakl'`, then your program should print: <br>

    Number of times bob occurs is: 2

### Solution

<hr>

[Problem 2](Problem2.py)

    # -*- coding: utf-8 -*-
    """
    Created on Wed Jun 21 12:35:21 2023
    
    @author: Cristian David Polo Garrido
    """
    
    def bob(s):
        pos=0
        bob=0
        while (pos<len(s)):
            if(s[pos]=='b' and (pos+1 < len(s))):
                if(s[pos+1]=='o' and (pos+2 < len(s))):
                    if(s[pos+2]=='b'):
                        bob+=1
            pos+=1
        print('Number of times bob occurs is: '+str(bob))

<br>

### Problem 3

<hr>

Assume `s` is a string of lower case characters. <br>

Write a program that prints the longest substring of `s` in which the letters occur in alphabetical order. <br>
For example, if `s = 'azcbobobegghakl'`, then your program should print: <br>

    Longest substring in alphabetical order is: beggh

<br>

In the case of ties, print the first substring. For example, if `s = 'abcbcd'`, then your program should print: <br>

    Longest substring in alphabetical order is: abc
    
<br>

**Note**: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.

<br>

### Solution

<hr>

[Problem 3](Problem3.py)

    # -*- coding: utf-8 -*-
    """
    Created on Wed Jun 21 12:40:43 2023
    
    @author: Cristian David Polo Garrido
    """
    
    def substring(s):
        min = 0
        substring = []
        for i in range(len(s)):
            cont = 0
            for j in range(i+1,len(s)):
                if ord(s[i+cont]) <= ord(s[j]):
                    cont += 1
                else:
                    break
            cont += 1
            min = max(cont,min)
            substring.append(cont)
            
        for i in range(len(substring)):
            if substring[i] == min:
                print(s[i:i+substring[i]])
                break
