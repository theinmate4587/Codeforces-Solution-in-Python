# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:19:27 2020

@author: Harshal
"""

n=int(input())
arr=list(map(int,input().split()))
temp=sorted(arr)
l=-1
r=-1

for i in range(n):
    if arr[i]!=temp[i]:
        l=i
        break

for i in range(n-1,-1,-1):
    if arr[i]!=temp[i]:
        r=i
        break

if r==l==-1:
    print("yes")
    print(1,1)
else:
    arr=arr[:l]+arr[l:r+1][::-1]+arr[r+1:]
   
    if temp==arr:
        print("yes")
        print(l+1,r+1)
    else:
        print("no")