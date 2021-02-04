# 1018번 : 체스판 다시 칠하기

import sys
n, m = map(int, input().split())

w = ['WBWBWBWB' if i%2 == 0 else 'BWBWBWBW' for i in range(8)]
b = ['BWBWBWBW' if i%2 == 0 else 'WBWBWBWB' for i in range(8)]

chess = []
for _ in range(n):
    chess += [sys.stdin.readline().strip()]

result = []
temp_chess = []
for j in range(m-7):
    for i in range(n-7):
        temp = []
        for l in range(8):
            temp += [chess[l+i][j:j+8]]
        temp_chess += [temp]

for tc in temp_chess:
    w_temp = 0
    b_temp = 0
    for i in range(8):
        for j in range(8):
            if w[i][j] != tc[i][j]:
                w_temp += 1
            if b[i][j] != tc[i][j]:
                b_temp += 1
            
    result.extend([w_temp, b_temp])
print(min(result))