n,m=map(int,input().split())
s=set()
r=''
p=''
for _ in range(n):
	c = input()
	if c[::-1]==c:
		p=c
	if c[::-1] in s:
		r+=c
	else:
		s.add(c)
r=r+p+r[::-1]
print(len(r))
print(r)