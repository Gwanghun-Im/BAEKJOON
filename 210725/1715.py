import heapq

N = int(input())
h = []
for _ in range(N):
    heapq.heappush(h, int(input()))

ans = 0
while h:
    x = heapq.heappop(h)
    if h: 
        y = heapq.heappop(h)
        ans += (x+y)
        heapq.heappush(h, x+y)

print(ans)
