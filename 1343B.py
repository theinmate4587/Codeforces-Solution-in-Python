# -*- coding: utf-8 -*-
"""
Created on Mon May 11 08:11:49 2020

@author: Harshal
"""


t=int(input())
for i in range(t):
    n=int(input())
    a=n//2
    if a%2==1:
        print("NO")
        
    else:
        print("YES")
        odd=[]
        even=[]
        for i in range(2,n+1,2):
            even.append(i)
        for i in range(1,n-1,2):
                       
            odd.append(i)
        odd.append(odd[-1]+2+len(even))
        for i in even+odd:
            print(i,end=" ")
            