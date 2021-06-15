
N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
dp = [0]*(K+1)
dp[0] = 1
for c in coin:
    for i in range(c, K+1):
        if i-c >= 0: dp[i] += dp[i-c]
print(dp[K])