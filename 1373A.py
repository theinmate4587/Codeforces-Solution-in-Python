# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 09:27:32 2020

@author: Harshal
"""


test=int(input())
for _ in range(test):
    a,b,c=map(int,input().split())
    
    print(2*(a<c)-1,-1 if a*b<=c else b)
    