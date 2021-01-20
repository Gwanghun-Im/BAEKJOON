# 1010번 : 다리 놓기

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    answer = 1

    for i in range(a):
        answer *= (b-i)

    for i in range(1,a+1) :
        answer //= i
    
    print(answer)

