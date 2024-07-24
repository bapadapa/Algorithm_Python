# https://www.acmicpc.net/problem/27323

x, y, w, h = map(int, input().split())
print(min(x, y, (w - x), (h - y)))
