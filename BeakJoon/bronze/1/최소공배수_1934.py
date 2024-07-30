# https://www.acmicpc.net/problem/1934
import sys

data = sys.stdin.readlines()

for nums in data[1:]:
    x, y = map(int, nums.split())
    a, b = x, y
    while b:
        a, b = b, a % b
    print(x * y // a)
