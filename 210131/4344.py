# 4344번 : 평균은 넘겠지

n = int(input())

for _ in range(n):
    x = list(map(int, input().split()))
    num = x[0]
    del x[0]
    
    cnt = 0
    for i in x:
        if i > (sum(x)/num):
            cnt += 1
    print(f'{(cnt/num)*100:.3f}%')