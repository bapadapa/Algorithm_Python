bucket, tryCount = map(int, input().split())
balls = [0] * bucket

for _ in range(tryCount):
    i, j, k = map(int, input().split())
    balls[i - 1 : j] = [k] * (j - i + 1)
print(" ".join(map(str, balls)))
