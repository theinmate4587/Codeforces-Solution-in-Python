# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:13:21 2020

@author: Harshal
"""
import collections

n=int(input())
arr=[]
dic=collections.defaultdict(int)
for  _ in range(n):
    a,b=input().split()
    b=int(b)
    dic[a]+=b
    arr.append([a,dic[a]])
mx=max(dic.values())
for x,y in arr:
    if dic[x]==mx and y>=mx:
        print(x)
        break
