r, c = map(int, input().split())
pasture = [list(input()) for _ in range(r)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for y in range(r):
    for x in range(c):
        if pasture[y][x]=='W':
            for d in range(4):
                if 0<=(y + dy[d])<r and 0<=(x + dx[d])<c:
                    if pasture[y + dy[d]][x + dx[d]] == 'S':
                        print(0)
                        exit()
                    if pasture[y + dy[d]][x + dx[d]] == '.':
                        pasture[y + dy[d]][x + dx[d]] = 'D'
print(1)
for i in pasture:
    print(''.join(i))