# 1929번 : 소수 구하기

sieve = [1 for i in range(1000001)]
sieve[1] = 0

for i in range(2, 1000001):
    if sieve[i] == 0:
        continue
    for j in range(2*i, 1000001, i):
        sieve[j] = 0

a, b = map(int ,input().split())

for i in range(a, b+1):
    if sieve[i]:
        print(i)