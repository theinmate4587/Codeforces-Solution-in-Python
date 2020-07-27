# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:21:07 2020

@author: Harshal
"""


s=input()
arr=list(map(int,list(s)))
for i in range(len(arr)):
    if i==0 and arr[i]==9:
        continue
    if arr[i]>4:
        arr[i]=9-arr[i]
s=list(map(str,arr))
x=int(''.join(s))
print(x)

