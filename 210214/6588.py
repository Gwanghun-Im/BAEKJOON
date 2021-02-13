# 6588번 : 골드바흐의 추측

sieve = [1 for i in range(10000001)]
sieve[1] = 0
for i in range(2, 10000001):
    if sieve[i] == 0:
        continue
    for j in range(2*i, 10000001, i):
        sieve[j] = 0

def solve(n):
    for i in range(n):
            if sieve[i] == 0:
                continue
            for j in range(i, n):
                if sieve[j] == 0:
                    continue
                if i+j == n:
                    return f'{n} = {i} + {j}'
    return '"Goldbach\'s conjecture is wrong.\'"'

n = int(input())
while n != 0:
    print(solve(n))
    n = int(input())