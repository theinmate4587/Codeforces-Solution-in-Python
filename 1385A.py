# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 07:54:10 2020

@author: Harshal
"""


test=int(input())
for _ in range(test):
    arr=list(map(int,input().split()))
    
    arr.sort()
    
    if arr[1]!=arr[2]:
        print("NO")
    else:
        print("YES")
        print(arr[0],arr[0],arr[2])
    