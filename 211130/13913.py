import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().split())
arr = [[0, ''] for _ in range(100000 + 1)]
q = deque()
q.append(N)

def bfs():
    while q:
        index = q.popleft()
        if index == K:
            return arr[index][0], arr[index][1] + ' ' + str(K)

        for c in (index * 2, index - 1, index + 1):
            if c == index * 2 and 2 * K <= c:
                continue
            if 0 <= c <= 100000 and not arr[c][0]:
                arr[c][0] = arr[index][0] + 1

                arr[c][1] = arr[index][1] + ' ' + str(index)
                q.append(c)
        arr[index][1] = ''


n, ar = bfs()
ar = ar[1:]
print(n)
print(ar)
# print(*bfs())