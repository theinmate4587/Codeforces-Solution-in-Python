# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:25:50 2020

@author: Harshal
"""


n=int(input())
s=input()
mx=0
dic={}
dic2={}
for i in range(n-1):
    if s[i:i+2] in dic:
        dic[s[i:i+2]]+=1
        mx=max(mx,dic[s[i:i+2]])
    else:
        dic[s[i:i+2]]=1
        mx=max(mx,1)
for x,y in dic.items():
    dic2[y]=x
print(dic2[mx])
        