# https://www.acmicpc.net/problem/31403

import sys

data = sys.stdin.readlines()

print(int(data[0]) + int(data[1]) - int(data[2]))
print(int(data[0].strip() + data[1]) - int(data[2]))
