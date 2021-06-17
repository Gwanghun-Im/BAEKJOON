# 5430번: AC

r = [0,-1]
for _ in range(int(input())):
    p = input()
    n = int(input())
    arr = eval(input())
    flag = False
    for order in p:
        if order == 'D':
            try:
                arr.pop(r[flag])
            except:
                print('error')
                break
        else:
            flag = not flag
    else:
        print('[',end='')
        l = len(arr)
        if not arr:
            print(']')
        elif flag:
            for i in range(l-1, 0, -1):
                print(arr[i],end=',')
            print(f'{arr[0]}]')
        else:
            for i in range(l-1):
                print(arr[i],end=',')
            print(f'{arr[l-1]}]')