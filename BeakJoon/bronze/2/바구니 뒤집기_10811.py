bucket, tryCount = map(int, input().split())
balls = list(range(1, bucket + 1))

for _ in range(tryCount):
    start, end = map(int, input().split())
    balls[start - 1 : end] = balls[start - 1 : end][::-1]
print(" ".join(map(str, balls)))
