#1005번 : ACM Craft
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = [0 for i in range(N)]
    for i in range(K):
        s1 , s2 = map(int,input().split())
