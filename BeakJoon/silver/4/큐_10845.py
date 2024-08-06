# https://www.acmicpc.net/problem/10845
import sys
from collections import deque

data = sys.stdin.readlines()
l = deque()
for i in data[1:]:
    i = i.strip().split()
    if i[0] == "push":
        l.append(i[1])
    elif i[0] == "pop":
        print(l.popleft() if l else -1)
    elif i[0] == "size":
        print(len(l))
    elif i[0] == "empty":
        print(0 if l else 1)
    elif i[0] == "front":
        print(l[0] if l else -1)
    elif i[0] == "back":
        print(l[-1] if l else -1)
