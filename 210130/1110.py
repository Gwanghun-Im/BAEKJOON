# 1110번 : 더하기 사이클

n = input()

if len(n) == 1:
    n = '0' + n

nn = n[1] + str((int(n[0]) + int(n[1])) % 10)
cnt = 1
while nn != n:
    nn = nn[1] + str((int(nn[0]) + int(nn[1])) % 10)
    cnt += 1

print(cnt)