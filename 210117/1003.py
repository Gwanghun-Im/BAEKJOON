'''
def fibonacci(n):
    if n == 0 :
        global cnt_0
        cnt_0 += 1
        return 0
    elif n == 1:
        global cnt_1 
        cnt_1 += 1
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
for i in range(n):
    cnt_0 = 0
    cnt_1 = 0
    x = int(input())
    fibonacci(x)
    print(f'{cnt_0} {cnt_1}')
'''

#
def fib(n):
    if cache[n] == 0 and n > 2:
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    else :
        return cache[n]


cache = [0 for i in range(41)]
cache[0] = 0
cache[1] = 1
cache[2] = 1

n = int(input())
for i in range(n):
    x = int(input())
    if x == 1 :
        print(f'{0} {1}')
    elif x == 0:
        print(f'{1} {0}')
    else :
        fib(x)
        print(f'{cache[x-1]} {cache[x]}')