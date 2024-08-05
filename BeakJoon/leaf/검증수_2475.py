# https://www.acmicpc.net/problem/2475

import sys

print(sum([x**2 for x in map(int, sys.stdin.readline().split())]) % 10)
