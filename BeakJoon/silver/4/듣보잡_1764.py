# https://www.acmicpc.net/problem/1764
import sys

data = sys.stdin.readlines()
n, m = map(int, data[0].split())

result = sorted(set(data[1 : n + 1]) & set(data[n + 1 :]))
print(len(result))
print("".join(result))
