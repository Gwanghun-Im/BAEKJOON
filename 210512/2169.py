# 2169번: 로봇 조종하기
from heapq import heappop, heappush

def stand(x):
    return x-my_min


dy = [0, 1, 0]
dx = [-1, 0, 1]

N, M = map(int, input().split())

mars = [list(map(int, input().split())) for _ in range(N)]
dp = [[-float('inf')]*M for _ in range(N)]

my_min = 0
for i in range(N):
    for j in range(M):
        my_min = min(my_min, mars[i][j])

for i in range(N):
    mars[i] = list(map(stand, mars[i]))

dp[0][0] = mars[0][0]

heap = []
heappush(heap, [-dp[0][0], 0, 0, 3])
while heap:
    w, y, x, pre = heappop(heap)
    
    # 3의 경우는 존재하지 않음
    temp = 3
    # 이전의 진행방향이 왼쪽인 경우
    if pre == 0:
        # 오른쪽으로 갈 수 없다.
        temp = 2
    # 이전의 진행방향이 오른쪽인 경우
    elif pre == 2:
        # 왼쪽으로 갈 수 없다.
        temp = 0
    w = -w
    if dp[y][x] > w:
        continue
    for d in range(3):
        my = y + dy[d]
        mx = x + dx[d]
        if 0<=my<N and 0<=mx<M and temp != d:
            if dp[my][mx] < w+mars[my][mx] + my_min:
                dp[my][mx] = w+mars[my][mx] + my_min
                heappush(heap, [-(w+mars[my][mx]), my, mx, d])
    
for i in dp:
    print(*i)
