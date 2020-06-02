# -*- coding: utf-8 -*-
"""
Created on Mon May 11 07:42:41 2020

@author: Harshal
"""


n,l=input().split()
n=int(n)
l=int(l)
arr=list(map(int,input().split()))
arr.sort()
d=0.00
if arr[0]!=0:
    d=float(arr[0])
if arr[-1]!=l:
    d=max(d,l-arr[-1])
for i in range(1,len(arr)):
    d=max((arr[i]-arr[i-1])/2.00,d)
print(d)
