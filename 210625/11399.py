# 11399번: ATM
n = int(input())
time = list(map(int, input().split()))
time.sort()
ans = 0
pri = 0
for i in time:
    ans += pri + i
    pri += i
print(ans)