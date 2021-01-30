# 10872번 : 팩토리얼

def fact(n):
    if n == 0:
        return 1
    if n == 1:
        return n
    return n * fact(n-1)

n = int(input())
print(fact(n))