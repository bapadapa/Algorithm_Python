# https://www.acmicpc.net/problem/10813

bucket, tryCount = map(int, input().split())

balls = list(range(1, bucket + 1))

for _ in range(tryCount):
    i, j = map(int, input().split())
    balls[i - 1], balls[j - 1] = balls[j - 1], balls[i - 1]
print(" ".join(map(str, balls)))
