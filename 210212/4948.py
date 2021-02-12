# 4948번 : 베르트랑 공준

sieve = [1 for i in range(123456*2 + 1)]
for i in range(2, 123457):
    if sieve[i] == 0:
        continue
    for j in range(2 * i, 123456 * 2 + 1, i):
        sieve[j] = 0
        
n = int(input())
while n != 0:

    print(sum(sieve[n +1 : 2*n + 1]))
    n = int(input())
