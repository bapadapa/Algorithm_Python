# https://www.acmicpc.net/problem/10814


l = []
for _ in range(int(input())):
    l.append(list(map(str, input().split())))
for i in sorted(l, key=lambda x: int(x[0])):
    print(i[0], i[1])


import sys

print("".join(sorted(sys.stdin.readlines()[1:], key=lambda x: int(x.split()[0]))))
