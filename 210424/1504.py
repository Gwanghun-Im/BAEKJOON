# 1504번 : 특정한 최단 경로
from heapq import heappush, heappop

def dijkstra(node, k):
    dp = [float('inf') for _ in range(N)]
    dp[node] = k
    heap = []
    heappush(heap, (k, node))
    while heap:
        weight, num = heappop(heap)
        if dp[num] < weight:
            continue
        for n, w in s[num]:
            new_w = weight + w
            if dp[n] > new_w:
                dp[n] = new_w
                heappush(heap, (new_w, n))
    return dp

N, e = map(int, input().split())
s = [[]for _ in range(N)]
for i in range(e):
    u, v, w = map(int, input().split())
    s[u-1].append((v-1, w))
    s[v-1].append((u-1, w))

v1, v2 = map(int, input().split())
d0 = dijkstra(0, 0)
d_v1 = dijkstra(v1-1, d0[v1-1])
d_v2 = dijkstra(v2-1, d0[v2-1])
d_v1_v2 = dijkstra(v2-1, d_v1[v2-1])[-1]
d_v2_v1 = dijkstra(v1-1, d_v2[v1-1])[-1]
r = min(d_v1_v2, d_v2_v1) 
if r == float('inf'):
    r = -1
print(r)
