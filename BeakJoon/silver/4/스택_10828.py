# https://www.acmicpc.net/problem/10828
import sys

data = sys.stdin.readlines()
l = []
for i in data[1:]:
    i = i.strip().split()
    if i[0] == "push":
        l.append(i[1])
    elif i[0] == "pop":
        print(l.pop() if l else -1)
    elif i[0] == "size":
        print(len(l))
    elif i[0] == "empty":
        print(0 if l else 1)
    elif i[0] == "top":
        print(l[-1] if l else -1)
