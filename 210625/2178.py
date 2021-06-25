# 2178번 : 미로탐색
import heapq

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solve():
    h = []
    heapq.heappush(h, [1, 0, 0])
    while h:
        w, y, x = heapq.heappop(h)
        if y==N-1 and x==M-1:
            return w
        for d in range(4):
            my = y + dy[d]
            mx = x + dx[d]
            if 0<=my<N and 0<=mx<M and w+1 < dp[my][mx] and maze[my][mx]:
                heapq.heappush(h, [w+1, my, mx])
                dp[my][mx] = w+1


N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
dp = [[float('inf')]*M for _ in range(N)]
dp[0][0]=1
print(solve())