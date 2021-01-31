# 1546번 : 평균

n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
n_scores = [i/m*100 for i in scores]
print(sum(n_scores) / n)