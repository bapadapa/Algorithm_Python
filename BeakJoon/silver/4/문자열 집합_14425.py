# https://www.acmicpc.net/problem/14425
# import sys

# n, m = map(int, sys.stdin.readline().split())

# strN = []
# for _ in range(n):
#     strN.append(sys.stdin.readline())
# strN = set(strN)

# cnt = 0
# for _ in range(m):
#     if sys.stdin.readline() in strN:
#         cnt += 1
# print(cnt)


import sys

l = sys.stdin.readlines()
n, m = map(int, l[0].split())
s1 = set(l[1 : n + 1])
cnt = 0
for s in l[n + 1 :]:
    if s in s1:
        cnt += 1
print(cnt)
