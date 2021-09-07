N = int(input())
test_room = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for tr in test_room:
    answer += 1
    tr -= B
    if tr<=0:
        continue
    answer += (tr//C)
    if tr%C:
        answer += 1
print(answer)