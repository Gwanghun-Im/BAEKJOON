# 1978번 : 소수 찾기

sieve = [1 for i in range(1001)]
sieve[1] = 0

for i in range(2, 1001):
    if sieve[i] == 0:
        continue
    for j in range(i*2, 1001, i):
        sieve[j] = 0

n = int(input())
numbers = list(map(int, input().split()))

ans = 0
for i in numbers:
    ans += sieve[i]
print(ans)