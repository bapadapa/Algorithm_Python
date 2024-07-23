# https://www.acmicpc.net/problem/2720
for _ in range(int(input())):
    change = int(input())
    for cent in [25, 10, 5, 1]:
        print(change // cent, end=" ")
        change %= cent
