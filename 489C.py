# -*- coding: utf-8 -*-
"""

You have a positive integer m and a non-negative integer s.
Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. 
The required numbers should be non-negative integers written in the decimal base without leading zeroes.

Input:                           Input:    
2 15                             3 0

Output:                          Output:
69 96                            -1 -1

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
