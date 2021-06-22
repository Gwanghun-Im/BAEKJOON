# 2606번: 바이러스
from collections import deque

n = int(input())
q = deque()
q.append(1)
edges = [[] for _ in range(n+1)]
v = [0]*(n+1)
for _ in range(int(input())):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

while q:
    now = q.popleft()
    if not v[now]:
        v[now] = 1
        for i in edges[now]:
            if not v[i]:
                q.append(i)
print(sum(v)-1)