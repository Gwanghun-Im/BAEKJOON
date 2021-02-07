# 1342번 : 행운의 문자열

def is_lucky(x):
    for i in range(1, len(x)):
        if x[i-1] == x[i]:
            return False
    return True 

def next_permutation(nums):
    i = l = len(nums)-1
    while i > 0:
        if nums[i] > nums[i-1]:
            temp = 0
            for j in range(l, i-1, -1):
                if nums[j] > nums[i-1]:
                    temp = j
                    break
            nums[i-1], nums[temp] = nums[temp], nums[i-1]
            for j in range(i, i+1+(l-i)//2):
                nums[j], nums[l+i-j] = nums[l+i-j], nums[j]
            break
        i -= 1
    if i == 0:
        return(False)

    return(nums)

a = input()
num = []
for i in a:
    num += [ord(i)]
num.sort()
ans = 0
while num :
    if is_lucky(num):
        ans += 1
    num = next_permutation(num)

print(ans)
