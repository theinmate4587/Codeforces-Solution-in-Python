# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 09:58:42 2020

@author: Harshal
"""


n = list(input())
m = -1
for i, d in enumerate(n):
	if int(d) % 2 == 0:
		m = i
		if int(d) < int(n[-1]):
			break
if m < 0:
	print(-1)
else:
	n[-1], n[m] = n[m], n[-1]
	print(''.join(n))

        
