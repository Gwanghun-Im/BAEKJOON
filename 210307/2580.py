# 2580번 : 스도쿠

def fill_number(li):
    y = li[0]
    x = li[1]
    s = [i for i in range(1, 10)]
    for i in range(3):
        for j in range(3):
            if sdoku[(y//3)*3+i][(x//3)*3 + j] in s:
                s.remove(sdoku[(y//3)*3+i][(x//3)*3 + j])
    for i in range(9):
        if sdoku[y][i] in s:
            s.remove(sdoku[y][i])
        if sdoku[i][x] in s:
            s.remove(sdoku[i][x])
    return s

def dfs(n):
    global flag
    if n == len(empty):
        flag = 1
        return
    y, x = empty[n]
    empty_path = fill_number([y, x])
    for i in empty_path:
        sdoku[y][x] = i
        dfs(n+1)
        if flag:
            return
        sdoku[y][x] = 0

sdoku = [list(map(int, input().split())) for _ in range(9)]
empty = [(i, j) for i in range(9) for j in range(9) if not sdoku[i][j]]
flag = 0
dfs(0)
for i in sdoku:
    print(*i)
