# 1062번 : 가르침

n, k = map(int, input().split())
cnt = 0
for i in range(n):
    a = list(input())
    if len(set(a)) <= k: cnt+=1