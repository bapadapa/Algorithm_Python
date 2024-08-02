# https://www.acmicpc.net/problem/18258

# 시간 초과
# import sys

# data = sys.stdin.readlines()

# queue = []
# for i in data[1:]:
#     if i[:4] == "push":
#         queue.append(int(i.split()[1]))
#     elif i[:-1] == "pop":
#         if queue:
#             print(queue.pop(0))
#         else:
#             print(-1)
#     elif i[:-1] == "size":
#         print(len(queue))
#     elif i[:-1] == "empty":
#         print(0 if queue else 1)
#     elif i[:-1] == "front":
#         print(queue[0] if queue else -1)
#     elif i[:-1] == "back":
#         print(queue[-1] if queue else -1)

# https://www.acmicpc.net/problem/18258
import sys
from collections import deque

queue = deque()
for i in sys.stdin.readlines()[1:]:
    if i[:4] == "push":
        queue.append(int(i[4:]))
    elif i[:-1] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif i[:-1] == "size":
        print(len(queue))
    elif i[:-1] == "empty":
        print(0 if queue else 1)
    elif i[:-1] == "front":
        print(queue[0] if queue else -1)
    elif i[:-1] == "back":
        print(queue[-1] if queue else -1)
