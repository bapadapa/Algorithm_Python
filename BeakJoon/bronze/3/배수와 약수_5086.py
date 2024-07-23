# while True:
#     num1, num2 = map(int, input().split())
#     if num1 > num2:
#         if num1 % num2 == 0:
#             print("multiple")
#         else:
#             print("neither")
#     elif num1 < num2:
#         if num2 % num1 == 0:
#             print("factor")
#         else:
#             print("neither")
#     else : break

# v2
# 정리
while True:
    num1, num2 = map(int, input().split())
    if num1 == num2 == 0:
        break
    print(
        "multiple" if num1 % num2 == 0 else "factor" if num2 % num1 == 0 else "neither"
    )
