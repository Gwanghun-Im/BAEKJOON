# 1707번: 이분 그래프
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    q = deque()
    q.append(n)
    v[n] = 1
    while q:
        now = q.popleft()
        for i in edges[now]:
            if not v[i]:
                v[i] = -v[now]
                q.append(i)
            elif v[i] == v[now]:
                return False
    return True


for _ in range(int(input())):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    v = [0]*(V+1)
    for i in range(E):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    for i in range(1, V+1):
        if not v[i] and not bfs(i):
            print('NO')
            break
    else:
        print('YES')