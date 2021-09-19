N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
func = ['up','down','left','right']
answer = 0

def up(n):
    pass
def left(b, n):
    global answer, N
    for i in range(N):
        temp = []
        j = 0
        while j+1 < N:
            if b[i][j] == b[i][j+1]:
                temp.append(b[i][j]*2)
                j += 2
            else:
                temp.append(b[i][j])
                j += 1
        temp.append(b[i][j])
        b[i] = temp+[0]*(N-len(b)+1)
    return b

print(left(board, 0))