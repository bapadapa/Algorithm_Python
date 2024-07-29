# https://www.acmicpc.net/problem/2751
# 최초에는 input()으로 입력을 받았는데,  sys.stdin.readline() 보다 상대적으로 속도가 느려 시간초과가 발생함
import sys

nums = []
for _ in range(int(sys.stdin.readline())):
    nums.append(int(sys.stdin.readline()))
nums.sort()
print("\n".join(map(str, nums)) + "\n")
