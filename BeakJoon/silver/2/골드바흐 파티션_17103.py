# https://www.acmicpc.net/problem/17103

# v2

import sys
import math


def is_prime_num(x):
    is_prime = [True] * (x + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime[i]:
            for j in range(i * i, x + 1, i):
                is_prime[j] = False
    return [x for x in range(x + 1) if is_prime[x]]


prime_list = is_prime_num(1000000)
prime_set = set(prime_list)
data = sys.stdin.readlines()

for i in data[1:]:
    num = int(i)
    cnt = 0
    for j in prime_list:
        if j > num // 2:
            break
        if num - j in prime_set:
            cnt += 1
    print(cnt)

# v2
# import sys
# import math

# num = [True] * 1000001
# num[0] = num[1] = False

# for i in range(2, int(math.sqrt(1000001)) + 1):
#     if num[i]:
#         for j in range(i * i, 1000001, i):
#             num[j] = False
# prime_list = [x for x in range(1000001) if num[x]]
# prime_set = set(prime_list)

# data = sys.stdin.readlines()

# for i in data[1:]:
#     num = int(i)
#     cnt = 0
#     for j in prime_list:
#         if j > num // 2:
#             break
#         if num - j in prime_set:
#             cnt += 1
#     print(cnt)


# v3
# import sys

# num = [False] * 1000001
# num[0] = num[1] = True
# prime_list = []
# for i in range(2, 1000001):
#     if num[i] == False:
#         prime_list.append(i)
#         for j in range(i * i, 1000001, i):
#             num[j] = True
# prime_set = set(prime_list)

# data = sys.stdin.readlines()

# for i in data[1:]:
#     num = int(i)
#     cnt = 0
#     for j in prime_list:
#         if j > num // 2:
#             break
#         if num - j in prime_set:
#             cnt += 1
#     print(cnt)
