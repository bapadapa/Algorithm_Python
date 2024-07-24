# https://www.acmicpc.net/problem/24313

a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

print(+(a1 * n + a0 <= c * n and c >= a1))
