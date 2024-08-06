# https://www.acmicpc.net/problem/1676


def f(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans


for idx, num in enumerate(str(f(int(input())))[::-1]):
    if num != "0":
        print(idx)
        break
