# 12852번 : 1로 만들기 2

n= int(input())

result = [[] for _ in range(n+1)]
result[1] = 1

for i in range(2, n+1):
    a = result[i-1] + 1
    b = result[i//2] + 1 if not i%2 else n
    c = result[i//3] + 1 if not i%3 else n
    result[i] = min(a, b, c)


print(result[n]-1)

cnt_down = result[n]
now = n
li = [n]
while cnt_down: 
    cnt_down -= 1
    if result[now-1] == cnt_down:
        now -= 1
        li += [now]
        continue
    elif now%2==0 and result[now//2]==cnt_down:
        now //= 2
        li += [now]
        continue
    elif now%3 ==0 and result[now//3]==cnt_down:
        now //= 3
        li += [now]
        continue
print(*li)