# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:37:31 2020

@author: Harshal
"""

x,y,z=map(int,input().split())

score=0
score+=x-y

if z>=abs(score) and z!=0:
    print('?')
else:
    if score<0:
        print('-')
    elif score>0:
        print('+')
    else:
        print('0')