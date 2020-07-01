# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 07:35:31 2020

@author: Harshal
"""


n=int(input())
arr=['0']*10
s=input()
for i in s:
    if i=='L':
        for i in range(10):
            if arr[i]=='0':
                arr[i]='1'
                break
    elif i=='R':
        for i in range(9,-1,-1):
            if arr[i]=='0':
                arr[i]='1'
                break
    else:
        arr[int(i)]='0'
  
print(''.join(arr))
                
