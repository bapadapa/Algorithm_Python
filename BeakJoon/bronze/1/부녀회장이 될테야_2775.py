# https://www.acmicpc.net/problem/2775
# import sys

# data = sys.stdin.readlines()

# k = list(map(int, data[1::2]))
# n = list(map(int, data[2::2]))

# table = [list(x for x in range(1, 15))]
# for i in range(14):
#     tmp = []
#     nums = 0
#     for j in range(14):
#         nums += table[i][j]
#         tmp.append(nums)
#     table.append(tmp)

# for i in range(int(data[0])):
#     print(table[k[i]][n[i] - 1])

import sys

data = sys.stdin.readlines()

k = list(map(int, data[1::2]))
n = list(map(int, data[2::2]))

table = [[1 for _ in range(14)] for _ in range(15)]  # 매 1호는 1명
for i in range(14):  # 0층 값 삽입
    table[0][i] = i + 1
for i in range(1, 15):  # 0층 ~ 14층
    for j in range(1, 14):  # 2호 ~ 14호
        table[i][j] = table[i - 1][j] + table[i][j - 1]  # 규칙을 보면 이와 같음
for i in range(int(data[0])):
    print(table[k[i]][n[i] - 1])
