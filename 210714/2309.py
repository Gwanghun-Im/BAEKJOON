from itertools import permutations
messi = [int(input()) for _ in range(9)]
messi.sort()

for m in permutations(messi,7):
    if sum(m)==100:
        for i in m:
            print(i)
        break