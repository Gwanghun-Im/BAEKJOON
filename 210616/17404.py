# 17404번 : RGB거리 2

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
ans = 1000**2+1
for i in range(3):
    dp = [[0, 0, 0] for _ in range(N)]
    for j in range(3):
        if j==i:
            dp[0][j] = house[0][j]
            continue
        dp[0][j] = 1000**2
    for j in range(1, N):
        dp[j][0] = house[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = house[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = house[j][2] + min(dp[j-1][0], dp[j-1][1])
    dp[N-1][i] = float('inf')
    ans = min(ans, *dp[N-1])
print(ans)