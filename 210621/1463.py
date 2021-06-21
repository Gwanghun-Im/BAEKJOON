# 1463번: 1로 만들기
X = int(input())

dp = [0]*1000001

for i in range(2, X+1):
    a = dp[i-1]
    b = dp[i//3] if not i%3 else X
    c = dp[i//2] if not i%2 else X
    dp[i] = min(a, b, c)+1

print(dp[X])