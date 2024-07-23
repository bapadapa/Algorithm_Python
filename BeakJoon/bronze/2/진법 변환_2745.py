# https://www.acmicpc.net/problem/2745

# v1
n, b = input().split()
result = 0
for i, num in enumerate(n[::-1]):
    result += int(num) * int(b) ** i if num.isdigit() else (ord(num) - 55) * int(b) ** i
print(result)


# v2
# n, x = input().split()
# print(int(n, int(x)))
