# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:16:21 2020

@author: Harshal
"""


test=int(input())

for _ in range(test):
    n=int(input())
    s=input()
    l=1
    r=1
    sw=0
    for i in range(n-1):
        if s[i]>s[i+1]:
            sw=1
    if sw==0:
        print(s)
        continue
    
    for i in range(n):
        if s[i]=='1':
            l=i
            break
    for i in range(n-1,-1,-1):
        if s[i]=='0':
            r=i
            break
    print(s[:l]+'0'+s[r+1:])
        
        
        
            