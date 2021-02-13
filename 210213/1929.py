# 1929번 : 소수 구하기

a, b = map(int ,input().split())

sieve = [1 for i in range(b+1)]
sieve[1] = 0

for i in range(2, b+1):
    if sieve[i] == 0:
        continue
    for j in range(2*i, b+1, i):
        sieve[j] = 0

for i in range(a, b+1):
    if sieve[i]:
        print(i)