# 16198번 : 에너지 모으기

# def energy(x):
#     if len(x) == 3:
#         return(x[0] * x[-1])

#     else:
#         m = 0
#         idx = 0
#         for i in range(len(x)-2):
#             if x[i] * x[i+2] > m :
#                 m = x[i] * x[i+2]
#                 idx = i
#         del x[idx+1]
        
#         return m + energy(x)
# n = int(input())
# marble = list(map(int, input().split()))
# print(energy(marble))

from sys import stdin


def dfs(sum_bead):
    global answer

    if len(beads) == 2:
        answer = max(answer, sum_bead)
        return

    for i in range(1, len(beads) - 1):
        value = beads[i - 1] * beads[i + 1]
        origin = beads[i]
        del beads[i]
        dfs(sum_bead + value)
        beads.insert(i, origin)


if __name__ == '__main__':
    answer = 0
    n = int(stdin.readline())
    beads = list(map(int, stdin.readline().split()))
    dfs(0)
    print(answer)