# 3052번 : 나머지

result = set()
for _ in range(10):
    n = int(input())
    result.add(n % 42)

print(len(result))

