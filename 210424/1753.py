# 1753번 : 최단경로
from heapq import heappush, heappop

def dijkstra(node):
    dp[node] = 0
    heap = []
    heappush(heap, (0, node))
    while heap:
        weight, num = heappop(heap)
        if dp[num] < weight:
            continue
        for n, w in s[num]:
            new_w = weight + w
            if dp[n] > new_w:
                dp[n] = new_w
                heappush(heap, (new_w, n))

v, e = map(int, input().split())
k = int(input()) -1 
s = [[]for _ in range(v)]
dp = [float('inf') for _ in range(v)]
for i in range(e):
    u, v, w = map(int, input().split())
    s[u-1].append((v-1, w))
    
dijkstra(k)
for i in dp:
    if i == float('inf'):
        print('INF')
    else:
        print(i)