n = int(input())
m = n
ans = 0

while m > n//1.2 :
    n_m = m

    for i in str(m):
        n_m += int(i)

    if n == n_m:
        ans = m
    m -= 1

print(ans)

