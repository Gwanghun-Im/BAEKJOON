# 10972번 : 다음 순열

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
        return(-1)

    return(nums)

n = input()
nums = list(map(int, input().split()))
new_nums = next_permutation(nums)
if new_nums == -1 :
    print(new_nums)
else :
    for i in new_nums:
        print(i, end=' ')