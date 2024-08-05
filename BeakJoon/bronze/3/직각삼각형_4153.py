# https://www.acmicpc.net/problem/4153

import sys

data = sys.stdin.readlines()

for i in data[:-1]:
    l = sorted(map(int, i.split()))
    print("right" if l[0] ** 2 + l[1] ** 2 == l[2] ** 2 else "wrong")
