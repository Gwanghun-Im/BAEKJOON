dp = [[0]*3 for _ in range(100001)]
dp[1][0]=1
dp[2][1]=1
dp[3][1]=1
dp[3][0]=1
dp[3][2]=1
for i in range(4,100001):
    for j in range(3):
        dp[i][j] = (dp[i-j-1][(j+1)%3] + dp[i-j-1][(j+2)%3])%1000000009
for i in range(int(input())):
    print(sum(dp[int(input())])%1000000009)