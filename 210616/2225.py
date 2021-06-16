N, K = map(int, input().split())
dp = [0]*201
dp[1] = 1

for i in range(2, K+1):
    dp[i] = ((dp[i-1]*(N+i-1))//(i-1))
print(dp[K]%1000000000)