# 5021번 : 왕위 계승
from collections import Counter

N, M = map(int, input().split())
family_tree = {}
family_tree[input()] = 1

names = []
candi = []
parent = {}
for _ in range(N):
    c, p1, p2 = input().split()
    parent[c] = [p1,p2]
    names += [c, p1, p2]
for _ in range(M):
    temp = input()
    names += [temp]
    candi += [temp]

print(Counter(names))
