# 1912번: 연속합
n = int(input())
li = list(map(int, input().split()))
dp = [0]*n
for i in range(n):
    dp[i] = (dp[i-1] + li[i]) if dp[i-1] + li[i] > li[i] else li[i]
print(dp)
print(max(dp))