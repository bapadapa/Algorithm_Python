# https://www.acmicpc.net/problem/18110

# import sys


# def r(n):
#     return int(n) + (1 if n - int(n) >= 0.5 else 0)


# data = sys.stdin.readlines()

# outlier = r(int(data[0]) * 0.15)
# nums = sorted(int(x.strip()) for x in data[1:])
# l = nums[outlier : int(data[0]) - outlier]
# print(0 if data[0].strip() == "0" else r(sum(l) / (int(data[0]) - 2 * outlier)))

import sys

data = sys.stdin.read().splitlines()
n = int(data[0])

if n == 0:
    print(0)
else:
    outlier = int(n * 0.15 + 0.5)
    nums = sorted(int(x) for x in data[1:])
    l = nums[outlier : n - outlier]
    print(int(sum(l) / (n - 2 * outlier) + 0.5))
