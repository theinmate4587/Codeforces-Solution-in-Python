# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:12:35 2020

@author: Harshal
"""

import collections
test=int(input())
for _ in range(test):
    n,m=map(int,input().split())
    res=[]
    gress=[0]*(n+1)
    dn=collections.defaultdict(list)
    
    for _ in range(m):
        d,x,y=map(int,input().split())
        if d==1:
            dn[x].append(y)
            gress[y]+=1
        res.append([d,x,y])
    zp=[i for i in range(1,n+1) if gress[i]==0]
    count=0
    p=[0]*(n+1)
    
    while zp:
        u=zp.pop()
        count+=1
        p[u]=count
        for v in dn[u]:
            gress[v]-=1
            if gress[v]==0:
                zp.append(v)
    if count==n:
        print("YES")
        for d,x,y in res:
            if d==1:
                print(x,y)
            elif p[x]<p[y]:
                print(x,y)
            else:
                print(y,x)
    else:
        print("NO")
                