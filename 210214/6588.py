# 6588번 : 골드바흐의 추측

import sys

sieve = [1 for i in range(1000001)]
sieve[1] = 0
shorten = int(1000001**(0.5))+1

for i in range(2, shorten):
    if sieve[i] == 0:
        continue
    for j in range(2*i, 1000001, i):
        sieve[j] = 0

def solve(n):
    for i in range(3, n, 2):
        if sieve[i] :
            if sieve[n-i] == 1:
                return f'{n} = {i} + {n-i}'

    return "Goldbach\'s conjecture is wrong."

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0: break
    print(solve(n))