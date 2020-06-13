# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:45:00 2020

@author: Harshal
"""

import collections

n=int(input())
graph=collections.defaultdict(list)
respect={}
for i in range(1,n+1):
    p,res=map(int,input().split())
 
    if p==-1:
        respect[i]=True
        continue
    graph[p].append(i)
    respect[i]= not res

ans=[]


for i in range(1,n+1):
    
        
    if respect[i]==False:
        n=len(graph[i])
        sums=0
        for no in graph[i]:
            sums+=int(respect[no])
        if sums==0:
            ans.append(i)
            
            
if len(ans)==0:
    print(-1)
else:
    print(*ans)
                
                
            
    
