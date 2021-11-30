import heapq

X, Y = map(int, input().split())
def solve():
    h = []
    v = [0]*100001
    v[X] = 1
    heapq.heappush(h, [0, X, str(X)])
    while heapq:
        w, now, ans = heapq.heappop(h)
        if now == Y:
            return w, ans
        if now*2<100001 and now*2 < Y*2 and not v[now*2]:
            heapq.heappush(h, [w+1, now*2, ans+' '+str(now*2)])
            v[now*2] = 1
        if 0<= now+1<100001 and not v[now+1]:
            v[now+1] = 1
            heapq.heappush(h, [w+1, now+1, ans+' '+str(now+1)])
        if 0<= now-1<100001 and not v[now-1]:
            v[now-1] = 1
            heapq.heappush(h, [w+1, now-1, ans+' '+str(now-1)])
w, ans = solve()
print(w)
print(ans)