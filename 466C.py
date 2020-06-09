# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:01:19 2020

@author: Harshal
"""


n=int(input())
arr=list(map(int,input().split()))
sums=sum(arr)
two=0
if sums%3 ==0:
    s=sums/3
    cur=0
    k=s*2
    one=0
    
    for x in arr[:-1]:
        cur=cur+x
        if cur==k:
            two+=one
        if cur==s:
            one+=1
print(two)
        
    