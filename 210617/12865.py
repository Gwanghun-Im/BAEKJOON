# 12865번 : 평범한 배낭

N, K = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]
wv.insert(0, [0, 0])
knapsack = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = wv[i][0]
        value = wv[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])