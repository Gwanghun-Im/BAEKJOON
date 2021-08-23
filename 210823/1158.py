N, K = map(int, input().split())
li = [i for i in range(1, N+1)]
print('<',end='')
for i in range(N-1):
    for i in range(K-1):
        li.append(li.pop(0))
    print(li.pop(0),end=', ')
print(str(li.pop(0))+'>')