# https://www.acmicpc.net/problem/24511

# import sys
# from collections import deque

# data = sys.stdin.readlines()

# q_s = data[1].split()
# l = data[2].split()
# q_l = deque(l[x] for x in range(len(l)) if q_s[x] == "0")

# for i in data[4].split():
#     q_l.appendleft(i)
#     print(q_l.pop(), end=" ")

# https://www.acmicpc.net/problem/24511

import sys
from collections import deque

data = sys.stdin.readlines()

q_l = deque(y for x, y in zip(data[1].split(), data[2].split()) if x == "0")

for i in data[4].split():
    q_l.appendleft(i)
    print(q_l.pop(), end=" ")
