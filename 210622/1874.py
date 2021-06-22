n = int(input())
ans = [int(input()) for _ in range(n)]
s = []
i = 1
r = ''
while i <= n:
    s.append(i)
    r += '+'
    while s and s[-1] == ans[0]:
        s.pop()
        ans.pop(0)
        r += '-'
    i += 1
if not s:
    for i in r:
        print(i)
else:
    print('NO')