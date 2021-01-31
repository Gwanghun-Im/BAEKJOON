# 4673번 : 셀프 넘버

def d(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total + n

cache = []
for i in range(1, 10001):

    cache += [d(i)]
    if i in cache:
        continue
    print(i)