from collections import deque
import sys

n = int(sys.stdin.readline())
nodes = [[] for _ in  range(n+1)]
parent = [0]*(n+1)
v = [0]*(n+1)
v[1] = 1

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

q = deque()
q.append(1)

while q :
    now = q.popleft()
    for i in nodes[now]:
        if not v[i]:
            v[i] = 1
            parent[i] = now
            q.append(i)

for i in parent[2:]:
    print(i)
