x, y = 0, 0
max = 0
for i in range(9):
    a = map(int, input().split())
    for j, k in enumerate(a):
        if k >= max:
            x, y, max = i, j, k
print(f"{max}\n{x+1} {y+1}")
