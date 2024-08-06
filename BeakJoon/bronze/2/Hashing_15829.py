# https://www.acmicpc.net/problem/15829
import sys

r = 31
M = 1234567891

data = sys.stdin.readlines()

result = 0
for idx, num in enumerate(data[1].strip()):
    result += (ord(num) - 96) * r**idx
print(result % M)
