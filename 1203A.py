# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 07:53:43 2020

@author: Harshal
"""


test=int(input())
for _ in range(test):
    n=int(input())
    arr=list(map(int,input().split()))
    if n<4:
        print("YES")
    else:
        i=arr.index(1)
        a=arr[:i+1][::-1]+arr[i+1:][::-1]
        b=arr[i:]+arr[:i]
        temp=[i for i in range(1,n+1)]
        if temp==a or temp==b:
            print("YES")
        else:
            print("NO")
        