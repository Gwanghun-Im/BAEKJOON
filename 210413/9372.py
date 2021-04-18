# 9372번 : 상근이의 여행

for _ in range(int(input())):
    n, m = map(int, input().split())
    country = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        country[a] += [b]
        