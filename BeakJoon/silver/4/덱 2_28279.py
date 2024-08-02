# https://www.acmicpc.net/problem/28279

from collections import deque
import sys

deck = sys.stdin.readlines()

q = deque()
for i in deck[1:]:
    if i[0] == "1":
        q.appendleft(int(i[1:]))
    elif i[0] == "2":
        q.append(int(i[1:]))
    elif i[0] == "3":
        print(q.popleft() if len(q) != 0 else -1)
    elif i[0] == "4":
        print(q.pop() if len(q) != 0 else -1)
    elif i[0] == "5":
        print(len(q))
    elif i[0] == "6":
        print(0 if len(q) != 0 else 1)
    elif i[0] == "7":
        print(q[0] if len(q) != 0 else -1)
    elif i[0] == "8":
        print(q[-1] if len(q) != 0 else -1)
