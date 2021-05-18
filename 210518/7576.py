from heapq import heappop, heappush

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def result():
    my_max = 0
    for y in range(M):
        if 0 in farm[y]:
            return -1
        my_max = max([my_max]+ farm[y])
    return my_max-1

N, M = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(M)]

h = []
ans = 0
for y in range(M):
    for x in range(N):
        if farm[y][x] == 1:
            heappush(h, (1, y, x))

while h:
    n, y, x = heappop(h)
    for d in range(4):
        my = y + dy[d]
        mx = x + dx[d]
        if 0<=my<M and 0<=mx<N:
            if farm[my][mx] > n+1 or not farm[my][mx]:
                farm[my][mx] = n+1
                heappush(h, (n+1, my, mx))


print(result())