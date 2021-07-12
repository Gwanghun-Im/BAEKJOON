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
            for j in range(2):
                dp[j][i] = max(dp[not j][i-1], dp[not j][i-2], dp[j][i-2]) + a[j][i]
        print(max(dp[0][-1], dp[1][-1]))