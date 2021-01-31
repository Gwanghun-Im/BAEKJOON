# 8958번 : OX퀴즈

n = int(input())
for _ in range(n):
    ox = input()

    score = 0
    temp = 0
    for i in ox:
        if i == 'O':
            temp += 1
            score += temp
        else:
            temp = 0

    print(score)
