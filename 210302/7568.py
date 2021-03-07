# 7568번 : 덩치
n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))

rank = []
for i in range(n):
    temp = 1
    for j in range(n):
        if i == j:
            continue
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            temp += 1
    rank += [temp]
print(*rank)