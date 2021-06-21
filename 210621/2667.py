# 2667번 : 단지번호 붙이기
from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
my_map = [list(map(int, list(input()))) for _ in range(N)]
v = [[0]*N for _ in range(N)]

q = deque()
n = 0
ans = []
for i in range(N):
    for j in range(N):
        if my_map[i][j] and not v[i][j]:
            v[i][j] = 1
            q.append([i, j])
            temp = 0
            while q:
                y, x = q.popleft()
                temp += 1
                for d in range(4):
                    my = y + dy[d]
                    mx = x + dx[d]
                    if 0<=my<N and 0<=mx<N and not v[my][mx] and my_map[my][mx]:
                        q.append([my, mx])
                        v[my][mx] = 1
            n += 1
            ans += [temp]

print(n)
for i in sorted(ans):
    print(i)