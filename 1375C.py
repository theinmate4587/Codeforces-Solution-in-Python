# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:15:10 2020

@author: Harshal
"""

test=int(input())

for _ in range(test):
    n=int(input())
    arr=list(map(int,input().split()))
    if arr[0]<arr[-1]:
        print("YES")
    else:
        print("NO")
    
    
