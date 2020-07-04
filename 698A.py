# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:37:12 2020

@author: Harshal
"""


n=int(input())
arr=list(map(int,input().split()))
dp=[[0]*3 for _ in range(n+1)]

for i in range(1,n+1):
    if arr[i-1]==0:
        dp[i][0]=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
    elif arr[i-1]==1 or arr[i-1]==3:
        dp[i][1]=max(dp[i-1][0],dp[i-1][2])+1
    elif arr[i-1]==2 or arr[i-1]==3:
        dp[i][2]=max(dp[i-1][0],dp[i-1][1])+1
        
print(n-max(dp[-1]))