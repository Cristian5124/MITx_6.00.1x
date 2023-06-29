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