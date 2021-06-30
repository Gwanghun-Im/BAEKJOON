# 11052번: 카드 구매하기
N = int(input())
cards = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = cards[0]
for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i] , cards[j-1]+dp[i-j])
print(dp[N])