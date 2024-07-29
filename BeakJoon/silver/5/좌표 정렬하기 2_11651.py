# https://www.acmicpc.net/problem/11651

# v1
# import sys
# l = []
# for _ in range(int(sys.stdin.readline())):
#     x, y = map(int, input().split())
#     l.append([y, x])
# l.sort()
# for i in range(len(l)):
#     print(l[i][1], l[i][0])

# v2
import sys

l = []
for _ in range(int(sys.stdin.readline())):
    l.append(list(map(int, input().split())))

for i in sorted(l, key=lambda x: (x[1], x[0])):
    print(i[0], i[1])
