for i in range(int(input())):
    PS = input()
    s = []
    for i in PS:
        if i == '(':
            s.append(i)
        elif i == ')':
            if s and s[-1] == '(':
                s.pop()
            else:
                print('NO')
                break
    else:
        if s:
            print('NO')
        else:
            print('YES')