# 1149번: RGB거리
N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
dp[0] = house[0]
for i in range(1, N):
    dp[i][0] = house[i][0] + min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = house[i][1] + min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = house[i][2] + min(dp[i-1][1],dp[i-1][0])

print(min(dp[-1]))