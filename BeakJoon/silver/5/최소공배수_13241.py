# https://www.acmicpc.net/problem/13241

import sys

x, y = map(int, sys.stdin.readline().split())
a, b = x, y
while b != 0:
    a = a % b
    a, b = b, a
print(x * y // a)
