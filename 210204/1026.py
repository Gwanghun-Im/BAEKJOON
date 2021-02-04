# 1026번 : 보물
import copy
n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

b = B.copy()

A.sort()
b.sort(reverse=-1)

result = 0
for i in range(n):
    result += A[i] * b[i]

print(result)