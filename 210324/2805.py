# 2805번 : 나무자르기

n, m = map(int, input().split())
li = list(map(int, input().split()))

li.sort(reverse=1)
t = li[0]
b = 0

while b <= t:
    h = (t+b)//2
    for i in range(n):
        if li[i] <= h:
            idx = i
            break
    else:
        idx = n
    now = sum(li[:idx]) - h*(idx)
    if now < m:
        t = h-1
    else :
        if now == m:
            print(h)
            exit()
        b = h+1

print(b-1)