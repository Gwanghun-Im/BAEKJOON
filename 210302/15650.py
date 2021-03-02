# 15650번 : N과 M(2)

def permutation(li):
    global n, m
    if li and len(li)==m:
        return print(*li)
    if not li:
        for i in range(1, n+1):
            permutation(li + [i]) 
    else :
        for i in range(li[-1], n+1):
            if i not in li:
                permutation(li + [i])

n, m = map(int, input().split())
li = []
permutation(li)