# https://www.acmicpc.net/problem/4134

import sys

data = sys.stdin.readlines()

for i in data[1:]:
    num = int(i)
    if num == 2:
        print(2)
        continue
    if num % 2 == 0:
        num += 1

    prime_num = num
