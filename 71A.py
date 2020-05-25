# -*- coding: utf-8 -*-
"""
Created on Fri May  8 09:25:31 2020

@author: Harshal
"""


t=int(input())
for i in range(t):
    a=list(input())
    if len(a)<11:
        print(''.join(a))
    else:
        n=len(a)
        print(a[0]+str(n-2)+a[-1])
    