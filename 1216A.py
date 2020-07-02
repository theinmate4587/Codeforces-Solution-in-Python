# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 07:49:27 2020

@author: Harshal
"""

n=int(input())
s=list(input())
ans=0
for i in range(0,n-1,2):
    x=s[i]
    y=s[i+1]
    if (x=='a' and y=='a') or (x=='b' and y=='b'):
        if x=='a':
            s[i+1]='b'
        else:
            s[i]='a'
        ans+=1
print(ans)
print(''.join(s))  