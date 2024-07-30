# https://www.acmicpc.net/problem/1269
import sys

data = sys.stdin.readlines()
a = set(data[1].split())
b = set(data[2].split())

print(len(a - b) + len(b - a))
