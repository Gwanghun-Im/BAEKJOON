# 1309번: 동물원

N = int(input())
dp = [[0, 0, 0] for _ in range(100001)]
dp[0][0] = 1
for i in range(1, N+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2])%9901
    dp[i][1] = (dp[i-1][0] + dp[i-1][2])%9901
    dp[i][2] = (dp[i-1][0] + dp[i-1][1])%9901
print(sum(dp[N])%9901)