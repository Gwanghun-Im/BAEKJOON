# 16194번: 카드 구매하기 2
N = int(input())
cards = list(map(int, input().split()))

dp = [float('inf')] * (N+1)
dp[0] = 0
dp[1] = cards[0]
for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i] , cards[j-1]+dp[i-j])
print(dp[N])