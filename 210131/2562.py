# 2562번 : 최댓값

numbers = []
for _ in range(9):
    numbers += [int(input())]

sort_numbers = sorted(numbers)
print(sort_numbers[-1])
print(numbers.index(sort_numbers[-1]) + 1)