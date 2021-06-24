# 13334번: 철로
import heapq
import sys; input=sys.stdin.readline

n = int(input())
line_ = [list(map(int, input().split())) for _ in range(n)]
d = int(input())

line = []
for h, o in line_:
    if abs(o - h) > d:
        continue
    line.append(sorted([h, o]))
line.sort(key=lambda x : x[1])

heap = []
cnt = 0
for h, o in line:
    if not heap:
        heapq.heappush(heap, [h, o])
    else:
        while heap and heap[0][0] < o-d:
            heapq.heappop(heap)
    heapq.heappush(heap, [h, o])
    cnt = max(cnt, len(heap))
print(cnt)