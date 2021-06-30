# 2156번: 포도주 시식
N = int(input())
dp = [[0,0,0] for _ in range(N)]

for i in range(N):
    wine = int(input())
    dp[i][0] = dp[i-1][1] + wine
    dp[i][1] = dp[i-1][2] + wine
    dp[i][2] = max(dp[i-1])
if N == 1:
    print(max(dp[0]))
else:
    print(max(dp[-1]+dp[-2]))