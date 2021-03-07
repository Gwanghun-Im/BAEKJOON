# 16198번 : 에너지 모으기

def dfs(li, n, p):
    if n == 3:
        result.append(p + li[0]*li[-1])
    for i in range(1, n-1):
        dfs(li[:i]+li[i+1:], n-1, p + li[i-1]*li[i+1])


n = int(input())
marble = list(map(int, input().split()))
result = []
dfs(marble, n, 0)
print(max(result))