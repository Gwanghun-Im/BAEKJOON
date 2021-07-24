import heapq
import sys ; input = sys.stdin.readline

N, K = map(int, input().split())

h = []
for _ in range(N):
    heapq.heappush(h, list(map(int, input().split())))

C = [int(input()) for _ in range(K)]
C.sort()

value = 0
selected = []

for i in range(K):
    while h and C[i] >= h[0][0]:
        m, v = heapq.heappop(h)
        heapq.heappush(selected, -v)
    if selected:
        value -= heapq.heappop(selected)
    elif not h:
        break
print(value)