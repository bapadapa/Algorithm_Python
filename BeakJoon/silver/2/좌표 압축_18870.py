# https://www.acmicpc.net/problem/18870

import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
nums = sorted(set(l))
nums_dict = {value: index for index, value in enumerate(nums)}
print(" ".join(str(nums_dict[value]) for value in l))
