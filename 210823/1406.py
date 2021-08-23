string = list(input())
s = []
for i in range(int(input())):
    cmd = input()
    if cmd == 'L':
        if string:
            s.append(string.pop())
    elif cmd == 'B':
        if string:
            string.pop()
    elif cmd == 'D':
        if s:
            string.append(s.pop())
    else:
        string.append(cmd[-1])
print(''.join(string)+''.join(s[::-1]))