import itertools
​
n = int(input())
sl = [list(map(int, input().split())) for _ in range(n)]
# 각 팀원의 인덱스
team = [i for i in range(n)]
# 팀에서 2//n 명만 뽑는 경우의 수-> 스타트 팀
teams = itertools.combinations(team, n//2)
# 그냥 큰값
result = 100000
for start in teams:
    print(start)
	# 링크팀 -> 차집합
    link = tuple(set(team) - set(start))
    temp = 0
    for i in range(n//2):
        for j in range(n//2):
            temp += sl[start[i]][start[j]] - sl[link[i]][link[j]]
            
    if abs(temp) < result:
        result = abs(temp)
​
print(result)