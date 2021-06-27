def dfs(idx, now, num):
    global N
    if num < dp[idx][now]:
        return
    dp[idx][now] = num
    if now < 1 and idx+1 < N:
        dfs(idx+1, now+1, num+li[idx+1])
    if idx+2 < N:
        dfs(idx+2, 0, num+li[idx+2])

N = int(input())
li = [int(input()) for _ in range(N)]
dp = [[0, 0] for _ in range(N)]
dfs(-1, -1, 0)
print(max(dp[-1]))