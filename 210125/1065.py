# 1065번 : 한수

n = int(input())

cnt = 0
for i in range(1, n+1):

    str_i = str(i)
    if len(str_i) <= 2:
        cnt += 1
    else :
        d = int(str_i[1]) - int(str_i[0])

        temp = True
        for j in range(2, len(str_i)):
            if int(str_i[j]) - int(str_i[j - 1]) != d:
                temp = False
                break
        if temp :
            cnt += 1

                

print(cnt) 
