# https://www.acmicpc.net/problem/10816


# 시간 초과
# import sys

# n, m = sys.stdin.readlines()[1::2]
# n_l = n.split()
# for i in m.split():
#     cnt = 0
#     print(n_l.count(i), end=" ")
#     if cnt != 0:
#         n_l.remove(i)

# 시간 초과
# import sys

# n, m = sys.stdin.readlines()[1::2]
# n_l = n.split()
# m_l = m.split()
# m_l_s = set(m_l)

# for num in n_l:
#     if num not in m_l_s:
#         n_l.remove(num)

# for i in m_l:
#     cnt = 0
#     print(n_l.count(i), end=" ")
#     if cnt != 0:
#         n_l.remove(i)

# 성공
# import sys

# n, m = sys.stdin.readlines()[1::2]
# result = {}
# for i in n.split():
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
# for i in m.split():
#     if i in result:
#         print(result[i], end=" ")
#     else:
#         print(0, end=" ")


import sys
from collections import Counter

n, m = sys.stdin.readlines()[1::2]
n_count = Counter(n.split())
for i in m.split():
    print(n_count[i], end=" ")
