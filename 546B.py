# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 08:32:16 2020

@author: Harshal
"""


n=int(input())
arr=list(map(int,input().split()))
arr.sort()

p=0
s=0
for x in arr:
    s+=max(0,p-x+1)
    p=max(p+1,x)
print(s)
    