# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:35:51 2020

@author: Harshal
"""


n=int(input())
arr=[]
for i in range(n):
    a,b=map(int,input().split())
    arr.append((a,b))
arr.sort(key=lambda x:(x[0],x[1]))
best=-1
for i in range(n):
    if best<=arr[i][1]:
        best=arr[i][1]
    else:
        best=arr[i][0]
print(best)
    
    