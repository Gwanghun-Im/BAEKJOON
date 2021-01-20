# 1009번 : 분산처리

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    # n_data = a ** b
    b = b % 4 + 4
    n_data = a ** b
    
    if n_data % 10 == 0:
        print(10)
    else:
        print(n_data % 10)