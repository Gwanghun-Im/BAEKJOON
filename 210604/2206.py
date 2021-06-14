# 2206번: 벽 부수고 이동하기

import heapq
import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
my_map = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dis = [[float('inf')]*M for _ in range(N)]

dis[0][0]=0

h = []
heapq.heappush(h, (0, 1 ,0, 0))
while h:
    wall, w, y, x = heapq.heappop(h)
    for d in range(4):
        my = y + dy[d]
        mx = x + dx[d]
        if 0<=my<N and 0<=mx<M and dis[my][mx] > w+1:
            if my_map[my][mx]==0:
                dis[my][mx] = w + 1
                heapq.heappush(h, (wall, w+1, my, mx))
            if my_map[my][mx]==1 and not wall:
                dis[my][mx] = w + 1
                heapq.heappush(h, (1, w+1, my, mx))

if dis[-1][-1]==float('inf'):
    print(-1)
elif not dis[-1][-1]:
    print(1)
else:
    print(dis[-1][-1])