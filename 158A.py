# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:09:02 2020

@author: Harshal
"""


n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort(reverse=True)

kthscore=arr[k-1]
ans=0
for i in arr:
    if i>=kthscore and i>0:
        ans+=1
print(ans)