# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 08:17:46 2020

@author: Harshal
"""


for i in range(int(input())):
    input()
    arr=list(map(int,input().split()))
    arr.sort()
    size=1
    ans=0
    for i in arr:
        if i==size:
            ans+=1
            size=1
        else:
            size+=1
    print(ans)