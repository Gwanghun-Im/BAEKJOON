# 2960번 : 에라토스테네스의 체

def sieve(N, K):
    sieve = [0 for i in range( N+1)]

    order = 1
    for i in range(2, N+1):
        if sieve[i] :
            continue
        for j in range(i, N+1, i):
            if sieve[j]:
                continue
            sieve[j] = 1
            if order == K:
                return j
            order += 1


N, K = map(int, input().split())
print(sieve(N, K))