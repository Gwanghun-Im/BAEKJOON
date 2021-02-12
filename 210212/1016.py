# 1016번 : 제곱 ㄴㄴ 수
import math

a, b = map(int, input().split())

sieve = [1 for i in range(a, b+1)]

for i in range(2, int(b**0.5)+1):
    squres = i**2
    temp = (math.ceil(a/squres) * squres) - a
    while temp <= b-a :
        sieve[temp] = 0
        temp += squres

result = sum(sieve)
print(result)