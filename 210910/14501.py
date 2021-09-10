N = int(input())
consulting = [list(map(int, input().split())) for _ in range(N)]
dp = [consulting[i][1] for i in range(N)]
dp += [0]

for i in range(N-1, -1, -1):
    if consulting[i][0]+i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], consulting[i][1] + dp[i+consulting[i][0]])
print(dp[0])