# https://www.acmicpc.net/problem/13909

# v1
# 창문이 1개가 더 열리는 수의 등차가 3 + 2n이다
n = int(input())

result = 1
cnt = 3
while n - cnt > 0:
    n -= cnt
    cnt += 2
    result += 1
print(result)

# 2
# n^2 마다 창문이 1개씩 더 열림
print(int(int(input()) ** 0.5))
