n = int(input())

for i in range(n):
    a, b= map(int,input().split())

    if a==0:
        a_money=0
    elif a==1:
        a_money=500
    elif a<4:
        a_money=300
    elif a<7:
        a_money=200
    elif a<11:
        a_money=50
    elif a<16:
        a_money=30
    elif a<22:
        a_money=10
    else:
        a_money = 0
    
    if b==0:
        b_money=0
    elif b==1:
        b_money=512
    elif b<4:
        b_money=256
    elif b<8:
        b_money=128
    elif b<16:
        b_money=64
    elif b<32:
        b_money=32
    else:
        b_money = 0
    print((a_money+b_money)*10000)