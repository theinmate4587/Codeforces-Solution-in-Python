# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 08:39:54 2020

@author: Harshal
"""


test=int(input())
for _ in range(test):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    w=list(map(int,input().split()))
    a.sort(reverse=True)
    w.sort()
    ii=k
    l=0
    r=n-1
    ans=0
    for i in range(k):
        if w[i]>1:
            ii=i
            break
        ans=ans+a[l]*2
        l+=1
    for u in range(k-1,ii-1,-1):
        i=w[u]
        ans+=a[l]+a[r]
        r=r-i+1
        l=l+1
    print(ans)