#2193번: 이친수
n= int(input())
dp = [[0, 0] for _ in range(91)]
dp[1][1]=1
dp[2][0]=1
for i in range(3,n+1):
    dp[i][0]=dp[i-1][0]+dp[i-1][1]
    dp[i][1]=dp[i-1][0]

print(sum(dp[n]))