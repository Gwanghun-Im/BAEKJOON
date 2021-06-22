N, K = map(int, input().split())
li = [int(input()) for _ in range(N)]
li.sort()
cnt = 0
while K > 0:
    now = li.pop()
    temp = K//now
    K -= now*temp
    cnt += temp

print(cnt)