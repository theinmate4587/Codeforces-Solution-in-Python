# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:02:17 2020

@author: Harshal
"""


m,s=[int(i) for i in input().split()]
if (s==0 and m!=1) or s>9*m:
    print(-1,-1)
else:
    a=(10**((s-1)//9)*((s-1)%9+1))-1+10**(m-1)
    b=(10**m)-(10**(m-(s-1)//9-1))*(10-(s-(s-1)//9*9))
    print(int(a),b)
    