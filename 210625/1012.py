# 1012번: 유기농 배추
from collections import deque
import sys; input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    v[y][x] =1
    q = deque()
    q.append([y, x])
    while q:
        ny, nx = q.popleft()
        for d in range(4):
            my = ny +dy[d]
            mx = nx +dx[d]
            if 0<=my<N and 0<=mx<M and not v[my][mx] and filed[my][mx]:
                q.append([my, mx])
                v[my][mx] = 1


for _ in range(int(input())):
    M, N, K = map(int, input().split())
    
    filed = [[0]*(M) for _ in range(N)]
    v = [[0]*M for _ in range(N)]

    for i in range(K):
        x, y = map(int, input().split())
        filed[y][x] = 1
    
    cnt = 0
    for y in range(N):
        for x in range(M):
            if not v[y][x] and filed[y][x]:
                bfs(y, x)
                cnt += 1
    
    print(cnt)