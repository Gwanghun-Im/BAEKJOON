# 1002번 : 터렛
import math

x = int(input()) # 테스트의 개수
answer = [0 for i in range(x)]
for  i in range(x):
    y = list(map(int, input().split()))
    d1 = math.sqrt((y[0]-y[3])**2 + (y[1]-y[4])**2)
    d2 = y[2] + y[5]
    if d1 == 0 :
        if y[2] == y[5]:
            answer[i] = -1
        else :
            answer[i] = 0
    elif d1 == d2 :
        answer[i] = 1
    elif d1 > d2 :
        answer[i] = 0
    elif abs(y[2] - y[5]) > d1 :
        answer[i] = 0
    elif abs(y[2] - y[5]) == d1:
        answer[i] = 1
    else :
        answer[i] = 2

for i in range(x):
    print(answer[i])