# https://www.acmicpc.net/problem/4949
# import sys
# import re

# data = sys.stdin.readlines()
# # 비교를 위해 생성
# check = {"(": ")", "[": "]"}
# for i in data:
#     if i == ".\n":  # .은 EOF
#         break
#     l = []
#     is_balance = True
#     for b in re.sub("[^()\[\]]", "", i):  # ()[] 만 남김
#         if b in [")", "]"]:
#             # 순서와 짝이 맞아야 하고, 괄호 열기 전에 닫으면 안됨
#             # pop을 이용하여 마지막 요소를 호출하면서 제거
#             if len(l) == 0 or check[l.pop()] != b:
#                 is_balance = False
#                 break
#         else:
#             l.append(b)
#     # 괄호 여는게 더 많을 수 있기 때문에 길이 조건 추가
#     print("yes" if is_balance and len(l) == 0 else "no")

import sys
import re

data = sys.stdin.readlines()
for i in data:
    if i == ".\n":  # .은 EOF
        break
    s = re.sub("[^()\[\]]", "", i)  # string으로 변환
    while "()" in s or "[]" in s:  # () [] 가 string에 존재할때까지 반복
        s = s.replace("()", "")  # 제거
        s = s.replace("[]", "")
    print("yes" if s == "" else "no")  # 공백이어야 균형
