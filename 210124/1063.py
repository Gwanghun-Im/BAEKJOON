k, s , n = input().split()

row = ['#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '#']
col = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '#']

king = [row.index(k[0]), col.index(k[1])]
stone = [row.index(s[0]), col.index(s[1])]


def R(x):
    return [x[0] + 1, x[1]]

def L(x):
    return [x[0] - 1, x[1]]

def B(x):
    return [x[0], x[1] - 1]

def T(x):
    return [x[0], x[1] + 1]

def RT(x):
    return [x[0] + 1, x[1] + 1]

def LT(x):
    return [x[0] - 1, x[1] + 1]

def RB(x):
    return [x[0] + 1, x[1] - 1]

def LB(x):
    return [x[0] - 1, x[1] - 1]

def is_stone(x, y, C):
    if x == y:
        y = eval(f'{C}(y)')
    return y
    


for i in range(int(n)):
    command = input()

    temp_king = eval(f'{command}(king)')
    temp_stone = is_stone(temp_king, stone, command)
    
    if (0 in temp_king) or (9 in temp_king) or (0 in temp_stone) or (9 in temp_stone) :
        continue
    king, stone = temp_king, temp_stone

print(f'{row[king[0]]}{col[king[1]]}')
print(f'{row[stone[0]]}{col[stone[1]]}')