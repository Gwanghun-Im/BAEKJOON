# 1004번 : 어린왕자
# 어린왕자와 장미를 포함한 원의 개수 - 어린왕자와 장미 모두를 포함하는 원의 개수

n1 = int(input())

for i1 in range(n1):
     x1,y1,x2,y2 = map(int, input().split())
     n2 = int(input())
     cnt = 0

     for i2 in range(n2):
          cx,cy,r = map(int, input().split())
          d1 = ((x1-cx)**2 + (y1-cy)**2)**0.5
          d2 = ((x2-cx)**2 + (y2-cy)**2)**0.5
          if d1 < r and d2 <r :
               cnt += 0
          elif d1 < r :
               cnt += 1
          elif d2 < r :
               cnt += 1
     print(cnt)