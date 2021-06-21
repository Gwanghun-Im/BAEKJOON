# 1260번 : DFS와 BFS
from collections import deque
N, M, V = map(int, input().split())
edges = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    edges[a][b] = 1
    edges[b][a] = 1

v1 = [0]*(N+1)
s = [V]
dfs = []
while s:
    now = s.pop()
    if not v1[now]:
        dfs.append(now)
        v1[now] = 1
        for i in range(N, 0, -1):
            if edges[now][i] and not v1[i]:
                s.append(i)

v2 = [0]*(N+1)
q = deque()
q.append(V)
bfs = []
while q:
    now = q.popleft()
    if not v2[now]:
        bfs.append(now)
        v2[now] = 1
        for i in range(1, N+1):
            if edges[now][i] and not v2[i]:
                q.append(i)
print(*dfs)
print(*bfs)