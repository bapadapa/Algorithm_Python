# https://www.acmicpc.net/problem/1735

# 시간 초과
# import sys

# data = sys.stdin.readlines()

# x1, x2 = map(int, data[0].split())
# y1, y2 = map(int, data[1].split())
# a, b = x2, y2

# n = x1 * y2 + y1 * x2
# d = x2 * y2
# mul = 2
# while mul <= min(d, n):
#     if d % mul == n % mul == 0:
#         d /= mul
#         n /= mul
#         mul = 2
#         continue
#     mul += 1
# print(int(n), int(d))

import sys

data = sys.stdin.readlines()

x1, x2 = map(int, data[0].split())
y1, y2 = map(int, data[1].split())

a = n = x1 * y2 + y1 * x2
b = d = x2 * y2
gcd = 0
while d:
    n, d = d, n % d
    gcd = n
print(int(a / gcd), int(b / gcd))
