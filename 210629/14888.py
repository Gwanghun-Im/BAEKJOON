from itertools import permutations

def calc(li):
    now = nums[0]
    for i in range(n-1):
        now = int(eval(f'{now}{li[i]}{nums[i+1]}'))
    return int(now)


n = int(input())
nums = list(map(int, input().split()))

op = ['+','-','*','/']
sign = []
for i,j in enumerate(list(map(int, input().split()))):
    sign += [op[i]]*j
signs = list(set(permutations(sign)))

my_max = -float('inf')
my_min = float('inf')
for i in signs:
    temp = calc(i)
    my_max = max(my_max,temp)
    my_min = min(my_min,temp)
print(my_max)
print(my_min)