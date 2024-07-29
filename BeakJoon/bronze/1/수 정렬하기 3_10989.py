# https://www.acmicpc.net/problem/10989
# 메모리 제한으로 인해 최대 값이 10,000보다 작은 자연수니, 해당 개수만큼 list를 만들고, 순서대로 출력
import sys

nums = [0] * 10001

for _ in range(int(sys.stdin.readline())):
    nums[int(sys.stdin.readline())] += 1
for i in range(len(nums)):
    if nums[i] == 0:
        continue
    for _ in range(nums[i]):
        print(i)
