# https://www.acmicpc.net/problem/11650
import sys

l = []
for _ in range(int(sys.stdin.readline())):
    x, y = map(int, input().split())
    l.append([x, y])
l.sort()
for i in range(len(l)):
    print(l[i][0], l[i][1])
