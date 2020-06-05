# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:43:15 2020

@author: Harshal
"""


l,a,b,c=input().split()
l,a,b,c=int(l),int(a),int(b),int(c)
temp=[a,b,c]


dp=[-1]*(l+1)
dp[0]=0
for c in temp:
    for i in range(c,l+1):
        dp[i]=max(dp[i],dp[i-c]+1)

print(dp[-1])
        