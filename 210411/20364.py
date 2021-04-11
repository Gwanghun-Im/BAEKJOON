# 20364번 : 부동산 다툼

n, q = map(int, input().split())
duck = [int(input()) for _ in range(q)]

tree = [0] * (2**20+1)

for i in range(q):
    temp = duck[i]
    r = 0
    while temp:
        if tree[temp]:
            r = temp
        temp //= 2
    if not r:
        tree[duck[i]] = duck[i]
    print(r)
