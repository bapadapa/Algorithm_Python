# https://www.acmicpc.net/problem/10773

# import sys

# data = sys.stdin.readlines()  # 입력받은 인자를 각 list[str]로 받음
# data.pop(0)  # 최초 1회는 입력받을 개수이기 때문에 불필요
# l = []
# for i in data:
#     num = int(i)  # str이기 때문에 int로 형변환
#     if num == 0:  # 0이면 이전값 뺀다
#         l.pop()  # 이전값 추출
#         continue
#     l.append(num)  # 나머지는 삽입
# print(sum(l))  # 합산

import sys

data = sys.stdin.readlines()  # 입력받은 인자를 각 list[str]로 받음
l = []
for num in data[1:]:
    if num == "0\n":  # 0이면 이전값 뺀다
        l.pop()  # 이전값 추출
        continue
    l.append(int(num))  # 나머지는 삽입
print(sum(l))  # 합산


# 아래와 같이도 할 수 있긴하지만 비효율적이다
# import sys

# data = sys.stdin.readlines()  # 입력받은 인자를 각 list[str]로 받음
# data.pop(0)  # 최초 1회는 입력받을 개수이기 때문에 불필요
# point = 0
# while point < len(data):
#     if data[point].strip() == "0":  # realines는 마지막에 \n이 있어서 strip()으로 제거
#         data[point - 1 : point + 1] = []  # 0과 이전값 제거
#         point -= 1
#         continue
#     point += 1
# print(sum(map(int, data)))  # str int로 변환하여 합산
