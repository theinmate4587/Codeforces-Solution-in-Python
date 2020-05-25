# -*- coding: utf-8 -*-
"""
Created on Fri May  8 08:57:43 2020

@author: Harshal
"""


n,m,a=map(int,input().split())
l=(n-1)//a +1
w=(m-1)//a +1
print(l*w)