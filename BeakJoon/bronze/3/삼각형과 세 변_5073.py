# https://www.acmicpc.net/problem/5073

# while True:
#     lengths = list(map(int, input().split()))
#     lengths.sort()
#     if sum(lengths) == 0:
#         break
#     if lengths[2] >= lengths[0] + lengths[1]:
#         print("Invalid")
#         continue
#     print(["Equilateral", "Isosceles", "Scalene"][len({*lengths})])


# v2

while l := sum(lengths := list(map(int, input().split()))):
    print(
        ["Invalid", "Equilateral", "Isosceles", "Scalene"][
            (l > max(lengths) * 2) * len({*lengths})
        ]
    )
