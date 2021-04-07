# 1746번 : 듣보잡

n, m = map(int, input().split());r=sorted(list(set([input() for _ in range(n)]) & set([input() for _ in range(m)])));print(len(r))
for i in r:print(*i, sep='')