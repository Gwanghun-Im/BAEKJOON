# 8012번: 한동이는 영업사원

def order(node):
    global cnt
    if node.data == city[0]:
        city.pop(0)
        if not city:
            print(cnt)
            exit()
    for i in node.child:
        cnt += 1
        temp = city[0]
        order(nodes[i])
        if temp == city[0]:
            cnt -= 2
        cnt += 1

def find_root():
    p = [[i] for i in city]

    for i in range(len(city)):
        temp = nodes[city[i]]
        while True:
            tp = temp.parent
            if not tp:
                break
            p[i].append(tp)
            temp = nodes[temp.parent]
    r = []
    for pp in range(len(p)-1):
        flag = True
        for i in range(len(p[pp])):
            for j in range(len(p[pp+1])):
                if p[pp][i]==p[pp+1][j]:
                    r += [p[pp+1][j]]
                    flag = False
                    break
            if not flag:
                break
    kr = p[0]
    for i in range(1, len(p)):
        kr = list(set(kr)&set(p[i]))
    return kr, r

class Node:
    def __init__(self,data):
        self.data=data
        self.child = []
        self.parent = None

    def myadd(self,c):
        self.child += [c]

n = int(input())
road = [list(map(int, input().split())) for _ in range(n-1)]
m = int(input())
city = [int(input()) for _ in range(m)]

nodes = [Node(i) for i in range(n+1)]
visited = [False]*(n+1)
queue = [1]

cnt = 0
while road:
    dl = []
    for i in range(len(road)):
        if queue[0] in road[i]:
            temp = road[i]

            temp.remove(queue[0])
            nodes[queue[0]].myadd(temp[0])
            nodes[temp[0]].parent = queue[0]

            queue.append(temp[0])
            
            dl += [temp]
    for j in dl:
        road.remove(j)
    queue.pop(0)


kr,fr = find_root()
temp = nodes[kr[0]]
while True:
    tp = temp.parent
    if not tp:
        break
    cnt += 1
    temp = nodes[temp.parent]

order(nodes[kr[0]])
for i in fr:
    order(nodes[i])

'''
5
1 2
1 5
3 5
4 5
4
3
2
5
4
'''