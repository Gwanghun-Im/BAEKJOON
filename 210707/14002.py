# 14002번: 가장 긴 증가하는 부분수열

N = int(input())
A = list(map(int, input().split()))
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if A[i]>A[j]:
            dp[i] = max(dp[i],dp[j]+1)

my_max = max(dp)
print(my_max)
r= []

idx = N
while my_max:
    for i in range(idx-1, -1, -1):
        if dp[i]==my_max:
            if (r and r[-1] > A[i]) or not r:
                r.append(A[i])
                idx = i
                my_max -= 1
                break

print(*r[::-1])