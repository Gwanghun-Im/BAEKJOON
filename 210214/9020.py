# 9020번 : 골드바흐의 추측

sieve = [1 for i in range(10001)]
sieve[1] = 0
for i in range(2, 10001):
    if sieve[i] == 0:
        continue
    for j in range(2*i, 10001, i):
        sieve[j] = 0

def solve(n):
    for i in range(n//2, 0, -1):
            if sieve[i] == 0:
                continue
            for j in range(i, n):
                if sieve[j] == 0:
                    continue
                if i+j == n:
                    return f'{i} {j}'


T = int(input())
for _ in range(T):
    n = int(input())
    print(solve(n))
    
    
