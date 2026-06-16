# cook your dish here
n,m = map(int,input().split())

grph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    grph[u].append(v)
    grph[v].append(u)
    
visited = [False]*(n+1)
cnt = 0

for node in range(1,n+1):
    if not visited[node]:
        cnt += 1
        
        stack = [node]
        visited[node] = True
        
        while stack:
            curr = stack.pop()
            for nghbr in grph[curr]:
                if not visited[nghbr]:
                    visited[nghbr] = True
                    stack.append(nghbr)
print(cnt)
    
