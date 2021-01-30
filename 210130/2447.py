# 2447번 : 별 찍기 - 10
import pprint

def star(n, x, y, t):
    global draw
    if n == 3:
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if i == x + 1 and j == y + 1:
                    continue
                draw[i][j] = t
    else :
        star(n // 3, x, y, t)
        star(n // 3, x, y + n // 3, t)
        star(n // 3, x, y + n // 3 * 2, t)
        star(n // 3, x + n // 3, y, t)
        star(n // 3, x + n // 3, y + n // 3, 0)
        star(n // 3, x + n // 3, y + n // 3 * 2, t)
        star(n // 3, x + n // 3 * 2, y, t)
        star(n // 3, x + n // 3 * 2, y + n // 3, t)
        star(n // 3, x + n // 3 * 2, y + n // 3 * 2, t)


n = int(input())
draw = [[0 for i in range(n)]for j in range(n)]
star(n, 0, 0, 1)

for i in range(len(draw)):
    for j in range(len(draw[i])):
        if draw[i][j]:
            print('*', end='')
        else :
            print(' ', end='')
    print()