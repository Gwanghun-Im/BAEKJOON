# 1011번 : Fly me ro to the Alpha Centauri

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    
    goal = y - x
    
    cnt = 1
    travel_distance = 1
    move = 1

    while travel_distance < goal:
        travel_distance += move
        if cnt % 2:
            move += 1
        cnt += 1


    print(cnt)

