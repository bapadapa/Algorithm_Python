# https://www.acmicpc.net/problem/9063

xMin, yMin, xMax, yMax = 0, 0, 0, 0
n = int(input())
is_first = True
for _ in range(n):
    x, y = map(int, input().split())
    if is_first:
        xMin, yMin, xMax, yMax = x, y, x, y
        is_first = False
        continue
    xMin = min(xMin, x)
    yMin = min(yMin, y)
    xMax = max(xMax, x)
    yMax = max(yMax, y)
if n == 1:
    print(0)
else:
    print((xMax - xMin) * (yMax - yMin))
