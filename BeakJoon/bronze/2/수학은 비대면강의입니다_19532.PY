# https://www.acmicpc.net/problem/19532

a, b, c, d, e, f = map(int, input().split())

y = ((f * a) / d**2 - c * d) / (e * a - b * d)
x = (f - e * y) / d
print(x, y)

y = ((d * c) / a - a * f) / (d * b - a * e)
x = (f - e * y) / d
print(x, y)
