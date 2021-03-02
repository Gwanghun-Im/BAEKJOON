# 15649번 : N과 M(1)

def permutation(li ,n, m):
    if li and len(li) == m:
        print(*li)
    for i in range(1, n+1):
        if not li:
            permutation(li + [i], n, m)
        elif i not in li:
            permutation(li + [i], n, m)


n, m = map(int, input().split())
li = []
permutation(li, n, m)