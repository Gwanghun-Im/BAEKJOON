N = int(input())
conference = [list(map(int, input().split())) for _ in range(N)]
conference.sort(key=lambda x :(x[1],x[0]))

cnt = 0
end = 0
for s, e in conference:
    if s >= end:
        end = e
        cnt += 1
print(cnt)