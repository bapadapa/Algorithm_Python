# https://www.acmicpc.net/problem/4134

import sys
import math


def is_prime_num(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


data = sys.stdin.readlines()
for i in data[1:]:
    num = int(i)
    while not is_prime_num(num):
        num += 1
    print(num)
