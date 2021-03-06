# 1929번 : 소수 구하기

a, b = map(int ,input().split())

# 최대 크기만큼 1로 채워진 배열생성
sieve = [1 for i in range(b+1)]
# 1은 소수가 아니다.
sieve[1] = 0

# 소수인 2부터 차례대로 넣음
# 시간을 줄이기 위해서 (b+1)**0.5를 해도 구할 수 있다.
for i in range(2, b+1):
    # 만약 현재 i가 소수가 아니라면 반복문 수행 안해도 댐
    if sieve[i] == 0:
        continue
    # 만약 소수라면 끝까지 배수를 지워준다.
    for j in range(2*i, b+1, i):
        sieve[j] = 0

for i in range(a, b+1):
    if sieve[i]:
        print(i)