# v1
print("v1")
numCount = int(input())
nums = list(map(int, input().split()))
target = int(input())
count = 0
for num in nums:
    if num == target:
        count += 1
print(count)

# v2
print("v2")
numCount = int(input())
nums = list(map(int, input().split()))
print(nums.count(int(input())))

# v3
print("v3")
input()
print(input().split().count(input()))
