# https://www.acmicpc.net/problem/10828

import sys

data = sys.stdin.readlines()
l = []
for a in data[1:]:
    command = a.split()
    if command[0] == "1":
        l.append(command[1])
    elif command[0] == "2":
        print(l.pop() if len(l) != 0 else -1)
    elif command[0] == "3":
        print(len(l))
    elif command[0] == "4":
        print(1 if len(l) == 0 else 0)
    else:
        print(l[-1] if len(l) != 0 else -1)
