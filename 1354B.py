# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 08:10:45 2020

@author: Harshal
"""


test=int(input())
for _ in range(test):
    s=input()
    buff=[-1]*3
    ans=float('inf')
    for i in range(len(s)):
        buff[int(s[i])-1]=i
        if buff[0]>-1 and buff[1]>-1 and buff[2]>-1:
            ans=min(ans,max(buff)-min(buff)+1)
    if ans!=float('inf'):
        print(ans)
    else:
        print(0)
        