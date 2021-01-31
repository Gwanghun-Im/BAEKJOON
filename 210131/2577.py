# 2577번 : 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)
result_list = [int(i) for i in result]
result_dict = {i:0 for i in range(10)}

for i in result_list:
    result_dict[i] += 1

for i in result_dict.values():
    print(i)
