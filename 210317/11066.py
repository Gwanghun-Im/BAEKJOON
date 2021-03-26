
# def solve(li, n):
#     global cost
#     print(li)
#     if len(li) == 2:
#         n += sum(li)
#         if n < cost:
#             cost = n
#     elif n > cost:
#         pass
#     else:
#         for i in range(1, len(li)-1):
#             temp = li.pop(i)
#             li[i-1]+=temp
#             solve(li, n + li[i-1])
#             li[i-1]-=temp
#             li[i]+=temp
#             solve(li, n + li[i])
#             li[i]-=temp
#             li.insert(i, temp)

# def dp(s, e):
#     global cost
#     if cache[s][e]:
#         return cache[s][e]
#     if e-s == 1:
#         cache[s][e] = files[s]+files[e]
#         return cache[s][e]
#     if e-s == 2:
#         if files[s] < files[e]:
#             cache[s][e] = files[s]*2+files[s+1]*2+files[e]
#         else :
#             cache[s][e] = files[s]+files[s+1]*2+files[e]*2
#         return cache[s][e]
#     for i in range(s+1, e-1):
#         cost= min(cost, (dp(s, i)+dp(i, e)))

import sys
Max = sys.maxsize

T = int(input())

for tc in range(T):
    k = int(input())
    files = list(map(int, input().split()))
    cache = [[0]*k for _ in range(k)]
    Sum = [0]
    for i in range(k):
        Sum += [Sum[-1]+files[i]]
    
    for d in range(1, k):
        for i in range(k-d):
            j = d+i
            cache[i][j] = Max
            for l in range(i, j):
                cache[i][j] = min(cache[i][j],cache[i][l]+cache[l+1][j] + Sum[j+1]-Sum[i])
    print(cache[0][k-1])