import sys; input = sys.stdin.readline
def isPossible(n):
    for i in numbers:
        if i in str(n):
            return False
    else:
        return True

N = int(input())
M = int(input())
numbers = list(input().split())

move = abs(100-N)

now = N
if len(numbers)==10 or (len(numbers) == 9 and '0' not in numbers):
    pass
else:
    while True:
        if isPossible(now):
            move = min(move, len(str(now))+abs(now-N))
            break
        else: now += 1

now = N

while now >= 0:
    if isPossible(now):
        move = min(move, len(str(now))+abs(now-N))
        break
    else: now -= 1

print(move)