# 11729번 : 하노이 탑 이동 순서

def hanoi(n, s, e, m):
    if n == 1:
        print(s, e)
    else:
        hanoi(n - 1, s, m, e) # 위 4개 1->2
        print(s, e) # 맨아래 1개 1->3
        hanoi(n - 1, m, e, s) # 위 4개 2->3

n = int(input())

print(2**n - 1)
hanoi(n, 1, 3, 2)


