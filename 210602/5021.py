# 5021번 : 왕위 계승
from collections import deque

N, M = map(int, input().split())
family_tree = {}
family_tree[input()] = 10000

parent = []
for _ in range(N):
    parent.append(input().split())

for _ in range(N):
    for c, p1, p2 in parent:
        if p1 not in family_tree.keys():
            family_tree[p1] = 0
        if p2 not in family_tree.keys():
            family_tree[p2] = 0
        family_tree[c] = (family_tree[p1]+family_tree[p2])/2

name = ''
blood = 0
for _ in range(M):
    temp = input()
    try:
        if blood<family_tree[temp]:
            name = temp
            blood = family_tree[temp]
    except:
        continue
print(name)