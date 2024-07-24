# https://www.acmicpc.net/problem/3009

# v1
x, y = [], []
x_result, y_result = 0, 0
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(3):
    if x.count(x[i]) == 1:
        x_result = x[i]
    if y.count(y[i]) == 1:
        y_result = y[i]
print(x_result, y_result)

# v2
x, y = [], []
for _ in range(3):
    a, b = map(int, input().split())

    if a in x:
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)

print(x[0], y[0])
