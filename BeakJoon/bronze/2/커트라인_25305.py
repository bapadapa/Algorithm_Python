# https://www.acmicpc.net/problem/25305

n, k = map(int, input().split())
print(sorted(map(int, input().split()), reverse=True)[k - 1])
