
def check():
    global R, C
    for i in range(R):
        for j in range(C):
            if feed[-(1+j)][i] != student[i][j]:
                return False
    return True

R, C = map(int,input().split())
feed = [list(map(int,input().split())) for _ in range(C)]
student = [list(map(int,input().split())) for _ in range(R)]

a = '''|>___/|     /}
| O O |    / }
( =0= )""""  \
| ^  ____    |
|_|_/    ||__|
'''
b = '''|>___/|        /}
| O < |       / }
(==0==)------/ }
| ^  _____    |
|_|_/     ||__|
'''
if check():
    print(b)
else:
    print(a)
