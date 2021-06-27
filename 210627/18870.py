# 18870번: 좌표 압축
N = int(input())
a = list(map(int, input().split()))
b = {j:i for i, j in enumerate(sorted(set(a)))}
ans = [0]*N
for i in range(N):
    ans[i] = b[a[i]]
print(*ans)