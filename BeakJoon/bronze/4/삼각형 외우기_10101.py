# https://www.acmicpc.net/problem/10101

# angle = []

# for _ in range(3):
#     angle.append(int(input()))
# if sum(angle) != 180:
#     print("Error")
# elif angle[0] == angle[1] == angle[2]:
#     print("Equilateral")
# elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
#     print("Isosceles")
# else:
#     print("Scalene")

# v2
angle = []
for _ in range(3):
    angle.append(int(input()))
print(
    # +(sum(angle) == 180) : 합이 180이면 1, 이외에는 0
    # 즉 합이 180이 아니면 0
    # len({*angle}) : list를 set으로 변환하여 중복을 제거한 후 길이를 반환
    # 각들이 3개다 중복이면 1, 2개 중복이면 2, 중복이 없으면 3
    ["Error", "Equilateral", "Isosceles", "Scalene"][
        (+(sum(angle) == 180) * len({*angle}))
    ]
)
