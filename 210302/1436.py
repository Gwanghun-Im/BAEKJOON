def solve(n):
    k = 0
    for i in range(666, 2666800):
        if '666' in str(i):
            k += 1
            if k == n:
                return(i)

n = input()
print(solve(int(n)))