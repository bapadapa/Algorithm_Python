# https://www.acmicpc.net/problem/11478
# import sys

# s = sys.stdin.readline()
# result = set()
# for i in range(len(s)):
#     for j in range(i, len(s)):
#         result.add(s[i:j])
# result.remove("")
# print(len(result))

import sys

s = sys.stdin.readline().strip()
result = set()
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        result.add(s[i:j])
print(len(result))
