
def checkBoard():
    global cnt, N
    for y in range(N):
        cnt_y, cnt_x = 1, 1
        for x in range(N):
            if x > 0:
                if board[y][x] == board[y][x-1]:
                    cnt_x += 1
                else:
                    cnt_x = 1

                if board[x][y] == board[x-1][y]:
                    cnt_y += 1
                else:
                    cnt_y = 1
            cnt = max(cnt, cnt_x, cnt_y)

N = int(input())
board = [list(input()) for _ in range(N)]
cnt = 0

for y in range(N):
    for x in range(N):
        if y < N-1 and board[y+1][x] != board[y][x]:
            board[y+1][x],board[y][x] = board[y][x],board[y+1][x]
            checkBoard()
            board[y+1][x],board[y][x] = board[y][x],board[y+1][x]
        if x < N-1 and board[y][x+1] != board[y][x]:
            board[y][x+1],board[y][x] = board[y][x],board[y][x+1]
            checkBoard()
            board[y][x+1],board[y][x] = board[y][x],board[y][x+1]

print(cnt)