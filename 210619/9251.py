# 9251번 : LCS
A = input()
B = input()
la = len(A)
lb = len(B)
dp = [[0]*1001 for _ in range(1001)]
for i in range(la):
    for j in range(lb):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

print(dp[la-1][lb-1])