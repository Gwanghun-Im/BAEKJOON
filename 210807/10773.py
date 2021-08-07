s = []
for i in range(int(input())):
    n = int(input())
    if n:
        s.append(n)
    else:
        s.pop()
print(sum(s))