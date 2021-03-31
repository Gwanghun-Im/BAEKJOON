# 1759번 : 암호 만들기
from itertools import combinations as cb

L, C = map(int, input().split())
li = list(map(ord, input().split()))
li.sort()

# 자음과 모음의 인덱스
cons_idx = []
vowel_idx = []
for i in range(C):
    # 'aeiou' 뽑아내기
    if li[i] in [97, 101, 105, 111, 117]:
        vowel_idx += [i]
    else:
        cons_idx += [i]

result = []

i = 1
j = L-i
# 자음의 개수가 2개 이상일때만
while j >= 2:
    # 조합 : 모음 i개와 자음 j개로 
    vo = list(cb(vowel_idx,i))
    co = list(cb(cons_idx,j))

    for v in vo:
        for c in co:
            # 인덱스 더해줌
            idxs = v + c
            r = []

            # 인덱스별로 추가
            for idx in idxs:
                r += [li[idx]]
            # 정렬
            r.sort()
            # 문자열로 만들어줌
            result += [list(map(chr, r))]
    # 자음과 모음개수 업데이트
    i += 1
    j = L-i

# 사전순으로 정렬
result.sort()
for i in result:
    print(*i, sep='')