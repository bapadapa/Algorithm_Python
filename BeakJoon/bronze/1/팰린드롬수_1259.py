# https://www.acmicpc.net/problem/1259

import sys

data = sys.stdin.readlines()
for i in data[:-1]:
    i = i.strip()
    print("yes" if i == i[::-1] else "no")
