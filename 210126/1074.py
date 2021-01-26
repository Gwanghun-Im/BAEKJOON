# 1074번 : Z
# 답은 나오는데 재귀 시간 드럽게 오래걸림 ㅡㅡ

import sys
N, r, c = map(int, sys.stdin.readline().split(' '))
cnt = 0

def Z(n, x, y):
    global cnt
    if n == 2:
        if x == r and y == c:
            print(cnt)
            exit()
            return
        cnt += 1
        if x == r and y + 1 == c: 
            print(cnt)
            exit()
            return
        cnt += 1
        if x + 1 == r and y == c:
            print(cnt)
            exit()
            return
        cnt += 1
        if x + 1 == r and y + 1 == c:
            print(cnt)
            exit()
            return
        cnt += 1

    else:
        Z(n // 2, x, y)
        Z(n // 2, x, y + n // 2)
        Z(n // 2, x + n // 2, y)
        Z(n // 2, x + n // 2, y + n // 2)

Z(2 ** N, 0, 0)