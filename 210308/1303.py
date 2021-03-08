# 1303번 : 전쟁-전투

n, m = map(int, input().split())
field = [list(input()) for _ in range(m)]
visited = [[False]*n for _ in range(m)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

power_W = 0
power_B = 0

for y in range(m):
    for x in range(n):
        if not visited[y][x]:
            soldier = field[y][x]
            visited[y][x] = True
            stack = [(y, x)]
            power = 0
            while stack:
                now = stack.pop()
                power += 1
                temp_y = now[0]
                temp_x = now[1]
                for i in range(4):
                    if (0<= temp_y+dy[i] < m) and (0 <= temp_x+dx[i] < n) and (not visited[temp_y+dy[i]][temp_x+dx[i]]) and (field[temp_y+dy[i]][temp_x+dx[i]] == soldier):
                        stack.append((temp_y+dy[i], temp_x+dx[i]))
                        visited[temp_y+dy[i]][temp_x+dx[i]] = True
            exec(f'power_{soldier} += power ** 2')
print(power_W, power_B)