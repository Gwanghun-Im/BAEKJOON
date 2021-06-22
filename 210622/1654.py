# 1654번: 랜선 자르기
K,N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
s, e = 0, max(lines)

while s<=e:
    mid = (s+e)//2
    temp = 0
    for i in lines:
        temp += i//mid
    if temp >= N:
        s = mid+1
    else:
        e = mid-1
print(e)