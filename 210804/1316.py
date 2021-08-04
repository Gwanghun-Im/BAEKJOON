
ans = 0
for _ in range(int(input())):
    word = input()
    temp = []
    l = len(word)
    i = 0
    while i < l:
        now = word[i]
        if now in temp :
            break
        i += 1
        while i < l and now == word[i]:
            i += 1
        else:
            temp += [now]
    else:
        ans += 1

print(ans)