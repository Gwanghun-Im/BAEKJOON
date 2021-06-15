alphabet = input()
li = [0]*123
for i in alphabet:
    li[ord(i)] += 1
print(*li[97:])