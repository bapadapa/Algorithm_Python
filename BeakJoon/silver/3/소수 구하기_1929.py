# https://www.acmicpc.net/problem/1929


# 시간 초과
# import sys
# import math


# def is_prime_num(x):
#     if x == 0 or x == 1:
#         return False
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if x % i == 0:
#             return False
#     return True


# data = sys.stdin.readlines()
# for i in data[:-1]:
#     num = int(i)
#     cnt = 0
#     for j in range(num + 1, 2 * num + 1):
#         cnt += is_prime_num(j)
#     print(cnt)


# 시간이 부족하니 미리 연산하고 처리함
import sys
import math


def is_prime_num(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


prime_num = [True] * (123456 * 2)

for i in range(len(prime_num)):
    prime_num[i] = is_prime_num(i)

data = sys.stdin.readlines()
for i in data[:-1]:
    num = int(i)
    print(sum(prime_num[num + 1 : 2 * num + 1]))
