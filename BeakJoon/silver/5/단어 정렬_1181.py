# https://www.acmicpc.net/problem/1181
import sys

l = []
for _ in range(int(sys.stdin.readline())):
    l.append(input())
l = list(set(l))
print("\n".join(sorted(l, key=lambda x: (len(x), x))))

# v2
import sys

l = list(set(sys.stdin.readlines()[1:]))
print("".join(sorted(l, key=lambda x: (len(x), x))))

# v3
import sys

print("".join(sorted(list(set(sys.stdin.readlines()[1:])), key=lambda x: (len(x), x))))
