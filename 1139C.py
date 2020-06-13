n,k=map(int,input().split())
g=[[] for _ in range(n+1)]

for i in range(n-1):
    u,v,x=map(int,input().split())
    if x == 0:
        g[u].append(v)
        g[v].append(u)
MOD=10**9  +7
vis=[0]*(n+1)
ans=pow(n,k)
for i in range(1,n+1):
    if vis[i]==0:
        cnt=0
        stack=[i]
        while stack:
            u=stack.pop()
            if vis[u]:
                continue
            vis[u]=1
            cnt+=1
            for v in g[u]:
                if not vis[v]:
                    stack.append(v)
        ans-=pow(cnt,k)
print(ans % MOD)