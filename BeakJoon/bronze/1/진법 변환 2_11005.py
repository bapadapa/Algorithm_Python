# https://www.acmicpc.net/problem/11005

n, b = map(int, input().split())

digit = 0
while b**digit <= n:
    digit += 1

for i in range(digit)[::-1]:
    if n // b**i < 10:
        print(n // b**i, end="")
    else:
        print(chr(n // b**i + 55), end="")
    n %= b**i
