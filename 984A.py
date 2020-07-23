# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 08:24:27 2020

@author: Harshal
"""


n=int(input())
arr=list(map(int,input().split()))
arr.sort()

while len(arr)>1:
    arr.pop()
    if len(arr)==1:
        break
    arr.pop(0)
print(arr[0])