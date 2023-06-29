bob=0
pos=0
cont=0
while (pos<len(s)):
    if(s[pos]=='b' and (pos+1 < len(s))):
       if(s[pos+1]=='o' and (pos+2 < len(s))):
           if(s[pos+2]=='b'):
               cont+=1
    pos+=1
print('Number of times bob occurs is: '+str(cont))