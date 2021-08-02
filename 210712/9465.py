for T in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(a[0][0], a[1][0]))
    if n == 2:
        print(max(a[0][0]+a[1][1],a[1][0]+a[0][1]))
    else:
        dp = [[0]*n for _ in range(2)]
        for i in range(n):
            dp[0][i] = max(dp[1][i-1], dp[0][i-2], dp[1][i-2]) + a[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2], dp[1][i-2]) + a[1][i]
        print(max(dp[0][n-1], dp[1][n-1]))