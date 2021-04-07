# 11725번 : 트리의 부모 찾기

n = int(input())
nodes = [0] * (n+1)
visited = [0] * (n+1)
visited[1] = 1

for i in range(n-1):
    a, b = map(int, input().split())
    if visited[a]:
        nodes[b] = a
    else:
        nodes[a] = b
    visited[a] = visited[b] = 1

for i in range(2, n+1):
    print(nodes[i])