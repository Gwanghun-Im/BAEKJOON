# 1365번 : 꼬인 전깃줄

n = int(input())
li = list(map(int, input().split()))
dp = [li[0]]

for i in range(1, n):
    temp = li[i]
    if dp[-1] < temp:
        dp.append(temp)
    else :
        for j in range(len(dp)):
            if dp[j] > temp:
                break
        dp[j] = temp
print(n-len(dp))