import sys

# nNums = []
# n = int(sys.stdin.readline())
# nNums = set(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())

# for num in map(int, sys.stdin.readline().split()):
#     if num in nNums:
#         print(1, end=" ")
#     else:
#         print(0, end=" ")


import sys

sang, jung = sys.stdin.readlines()[1::2]
sang = set(sang.split())
print(" ".join("1" if num in sang else "0" for num in jung.split()))
