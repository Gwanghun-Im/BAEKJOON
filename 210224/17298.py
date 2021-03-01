# 17298번 : 오큰수

n = int(input())
a = list(map(int, input().split()))

stack = [0]
ans = [-1]*n

for i in range(1, n):
    if not stack:
        stack.append(i)
    while stack and a[stack[-1]] < a[i]:
        ans[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)

print(*ans)