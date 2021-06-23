# 1655번: 가운데를 말해요

import heapq
import sys; input=sys.stdin.readline

N = int(input())
l, r = [], [int(input())]
print(r[0])
for _ in range(N-1):
    x = int(input())
    
    if x >= r[0]:
        heapq.heappush(r, x)
    else:
        heapq.heappush(l, -x)
    
    if len(r)-len(l) > 0:
        heapq.heappush(l, -heapq.heappop(r))
    
    if len(r)-len(l) < -1:
        heapq.heappush(r, -heapq.heappop(l))
    print(-l[0])