# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:10:27 2020

@author: Harshal
"""


n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
idx=[0]*n
cnt=[0]*n

for i in range(n):
    idx[a[i]-1]=i

for i in range(n):
    cnt[idx[b[i]-1]-i]+=1

print(max(cnt))