# -*- coding: utf-8 -*-
"""
Created on Tue May 26 10:06:02 2020

@author: Harshal
"""

import collections
n,k=list(map(int,input().split()))
cats=list(map(int,input().split()))
cats=[0]+cats
tree=collections.defaultdict(list)

for x in range(n-1):
    a,b=input().split()
    tree[int(a)].append(int(b))

ans=0
seen=set()
que=[(1,cats[1])]
while que:
    node,count=que.pop(0)
    if node not in tree and count<k:
        ans+=1
    elif count==k :
        seen.add(node)
    if node not in seen:
        for i in tree[node]:
            if cats[i]==0:
                que.append((i,0))
            else:
                que.append((i,count+1))
                
        
            
print(ans)
    