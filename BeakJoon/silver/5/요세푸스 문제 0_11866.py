# https://www.acmicpc.net/problem/11866

import sys

n, k = map(int, sys.stdin.readline().split())

l = [x for x in range(1, n + 1)]
idx = k - 1
result = []

# 최초 1회 삽입
result.append(l.pop(idx))
while l:
    idx = (idx + k - 1) % (len(l))
    result.append(l.pop(idx))

print(f"<{', '.join(map(str,result))}>")
