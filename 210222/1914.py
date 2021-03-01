# 1914번 : 하노이탑


def hanoi(n, s, e, m):
    if n == 1:
        print(s, e)
    else:
        hanoi(n - 1, s, m, e) # 위 4개 1->2
        print(s, e) # 맨아래 1개 1->3
        hanoi(n - 1, m, e, s) # 위 4개 2->3


n = int(input())

if n <= 20:
    print(2**n - 1)
    hanoi(n, 1, 3, 2)

else:
    print(2**n - 1)
