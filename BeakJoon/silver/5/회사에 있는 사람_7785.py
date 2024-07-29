# https://www.acmicpc.net/problem/7785

import sys

s = set()
for _ in range(int(sys.stdin.readline())):
    name, behavior = sys.stdin.readline().split()
    if behavior == "enter":
        s.add(name)
    else:
        s.remove(name)
print("\n".join(sorted(list(s), reverse=True)))
