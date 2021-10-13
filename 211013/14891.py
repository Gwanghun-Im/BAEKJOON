from collections import deque

ans = 0
gear = [deque(map(int, input())) for _ in range(4)]

for _ in range(int(input())):
    i, d = map(int, input().split())
    upper, upd, upi = i, d, gear[i-1][2]
    under, und, uni = i-2, d, gear[i-1][6]
    gear[i-1].rotate(d)

    while upper < 4:
        if upi != gear[upper][6]:
            upi = gear[upper][2]
            gear[upper].rotate(upd*-1)
            upd *= -1
            upper += 1
        else:break
        
    while under > -1:
        if uni != gear[under][2]:
            uni = gear[under][6]
            gear[under].rotate(und*-1)
            und *= -1
            under -= 1
        else:break

for i in range(4):
    if gear[i][0]:
        ans += (2**i)
print(ans)