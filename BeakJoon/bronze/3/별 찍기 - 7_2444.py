i = int(input())
j = 1
for _ in range(i * 2 - 1):
    print(" " * abs(i - j) + "*" * ((i - abs(i - j)) * 2 - 1))
    j += 1
