# -*- coding: utf-8 -*-
"""
Created on Fri May 15 09:33:32 2020

@author: Harshal
"""

leng,sums=list(map(int,input().split()))

def solve(cur,sums):
    
    if sums<0 or (len(cur)==leng and sums!=0):
        
        return 
    elif len(cur)==leng and sums==0:
        
        ans.append( int(cur))
        return
    for i in range(9,-1,-1):
        if sums-i<0:
            continue
        solve(cur+str(i),sums-i)
ans=[]
solve("",sums)
a=max(ans)
b=min(ans)
if a==0 and b==0:
    print(-1,end=" ")
    print(-1)
else:
    print(b,end=" ")
    print(a)