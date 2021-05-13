# 2169번: 로봇 조종하기
N, M = map(int, input().split())

mars = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

dp[0][0] = mars[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + mars[0][i]

for y in range(N-1):
    temp1 = [0]*M
    temp1[0] = dp[y][0] + mars[y+1][0]
    for x1 in range(1, M):
        temp1[x1] = max(temp1[x1-1]+mars[y+1][x1], dp[y][x1] + mars[y+1][x1])
    
    temp2 = [0]*M
    temp2[-1] = dp[y][-1] + mars[y+1][-1]
    for x2 in range(M-2, -1, -1):
        temp2[x2] = max(temp2[x2+1]+mars[y+1][x2], dp[y][x2] + mars[y+1][x2])
    for i in range(M):
        dp[y+1][i] = max(temp1[i], temp2[i])


# for y in range(N-1):
#     for i in range(M):
#         temp = [0]*M
#         temp[i] = dp[y][i] + mars[y+1][i]
#         for x1 in range(i+1, M):
#             temp[x1] = temp[x1-1]+mars[y+1][x1]
#             dp[y+1][x1] = max(dp[y+1][x1], temp[x1])
#         for x2 in range(i-1, -1, -1):
#             temp[x2] = temp[x2+1]+mars[y+1][x2]
#             dp[y+1][x2] = max(dp[y+1][x2], temp[x2])

print(dp[-1][-1])