# 1806번: 부분합

N, S = map(int, input().split())
li = list(map(int, input().split()))

s = 0
e = 1
now = li[s]
ans = float('inf') if now < S else 1

while not (s==e==N):
    if now < S and e < N:
        now += li[e]
        e += 1
    else:
        now -= li[s]
        s += 1
    if now >= S:
        ans = min(ans, e-s)

print(ans) if ans!=float('inf') else print(0)