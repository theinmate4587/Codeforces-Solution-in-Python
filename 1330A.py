for _ in range(int(input())):
	n, x = map(int,input().split())
	a = set(map(int,input().split()))
	i = 1
	while x > 0:
		if not( i in a ):
			x -= 1
		i += 1
	while i in a:
		i += 1
	print (i-1)