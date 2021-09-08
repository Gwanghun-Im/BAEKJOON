from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
flag = False
answer = -1

def up(r, b, n):
    global flag
    if r[0] > b[0]:
        by, bx = b
        while board[by][bx] == '.':
            by -= 1
        if board[by][bx] == 'O':
            return False
        by += 1
        ry, rx = r
        while board[ry][rx] == '.':
            ry -= 1
        if board[ry][rx] == 'O':
            flag = True
            answer = n
        else:
            ry += 1
        if [ry, rx] == [by, bx]:
            ry += 1
    else:
        ry, rx = r
        while board[ry][rx] == '.':
            ry -= 1
        if board[ry][rx] == 'O':
            flag = True
            answer = n
        else:
            ry += 1
        by, bx = b
        while board[by][bx] == '.':
            by -= 1
        if board[by][bx] == 'O':
            flag = False
            answer = -1
            return False
        by += 1
        if [ry, rx] == [by, bx]:
            by += 1
    if r == [ry, rx] and b == [by, bx]:
        return False
    return [[ry, rx], [by, bx], n+1]


def down(r, b, n):
    global flag
    if r[0] < b[0]:
        by, bx = b
        while board[by][bx] == '.':
            by += 1
        if board[by][bx] == 'O':
            return False
        by -= 1
        ry, rx = r
        while board[ry][rx] == '.':
            ry += 1
        if board[ry][rx] == 'O':
            flag = True
            answer = n
        else:
            ry -= 1
        if [ry, rx] == [by, bx]:
            ry -= 1
    else:
        ry, rx = r
        while board[ry][rx] == '.':
            ry += 1
        if board[ry][rx] == 'O':
            flag = True
            answer = n
        else:
            ry -= 1
        by, bx = b
        while board[by][bx] == '.':
            by += 1
        if board[by][bx] == 'O':
            flag = False
            answer = -1
            return False
        by -= 1
        if [ry, rx] == [by, bx]:
            by -= 1
    if r == [ry, rx] and b == [by, bx]:
        return False
    return [[ry, rx], [by, bx], n+1]

def left(r, b, n):
    global flag
    if r[1] > b[1]:
        by, bx = b
        while board[by][bx] == '.':
            bx -= 1
        if board[by][bx] == 'O':
            return False
        bx += 1
        ry, rx = r
        while board[ry][rx] == '.':
            rx -= 1
        if board[ry][rx] == 'O':
            flag = True
            answer = n
        else:
            rx += 1
        if [ry, rx] == [by, bx]:
            rx += 1
    else:
        ry, rx = r
        while board[ry][rx] == '.':
            rx -= 1
        if board[ry][rx] == 'O':
            flag = True
            answer = n
        else:
            rx += 1
        by, bx = b
        while board[by][bx] == '.':
            bx -= 1
        if board[by][bx] == 'O':
            flag = False
            answer = -1
            return False
        bx += 1
        if [ry, rx] == [by, bx]:
            bx += 1
    if r == [ry, rx] and b == [by, bx]:
        return False
    return [[ry, rx], [by, bx], n+1]

def right(r, b, n):
    global flag,O
    if r[1] < b[1]:
        by, bx = b
        while board[by][bx] == '.':
            bx += 1
        if board[by][bx] == 'O':
            return False
        bx -= 1
        ry, rx = r
        while board[ry][rx] == '.':
            rx += 1
        if board[ry][rx] == 'O':
            flag = True
            answer = n
        else:
            rx -= 1
        if [ry, rx] == [by, bx]:
            rx -= 1
    else:
        ry, rx = r
        while board[ry][rx] == '.':
            rx += 1
        if board[ry][rx] == 'O':
            flag = True
            answer = n
        else:
            rx -= 1
        by, bx = b
        while board[by][bx] == '.':
            bx += 1
        if board[by][bx] == 'O':
            flag = False
            answer = -1
            return False
        bx -= 1
        if [ry, rx] == [by, bx]:
            bx -= 1
    if r == [ry, rx] and b == [by, bx]:
        return False
    return [[ry, rx], [by, bx], n+1]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            B = [i, j]
            board[i][j] = '.'

q = deque()
q.append([R, B, 0])
while q:
    r, b, n = q.popleft()
    if n > 9:
        print(answer)
        break
    u = up(r, b, n)
    if u:
        q.append(u)
        if flag:
            print(u[-1])
            break
    d = down(r, b, n)
    if d:
        q.append(d)
        if flag:
            print(d[-1])
            break
    ri = right(r, b, n)
    if ri:
        q.append(ri)
        if flag:
            print(ri[-1])
            break
    l = left(r, b, n)
    if l:
        q.append(l)
        if flag:
            print(l[-1])
            break
else:
    print(answer)