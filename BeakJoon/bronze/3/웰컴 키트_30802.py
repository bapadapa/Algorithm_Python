# https://www.acmicpc.net/problem/30802
import sys
import math

data = sys.stdin.readlines()

n = int(data[0])
size = map(int, data[1].split())
t, p = map(int, data[2].split())

order = 0
for i in size:
    order += math.ceil(i / t)
print(order)
print(n // p, n % p)
