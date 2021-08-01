from collections import deque
N, K = map(int, input().split())

cage = [0]*1000001
q = deque()

max_x = 0
for i in range(N):
    g, x = map(int, input().split())
    cage[x] = g
    if x > max_x:
        max_x = x

temp = 0
answer = 0
for i in range(max_x+1):
    if len(q) < 2*K +1:
        q.append(cage[i])
        temp += cage[i]
        answer = temp
    else:
        temp -= q.popleft()
        q.append(cage[i])
        temp += cage[i]
        if temp > answer:
            answer = temp
print(answer)