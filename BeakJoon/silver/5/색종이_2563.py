board = [100 * [0] for _ in range(100)]
for _ in range(int(input())):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            board[x + i][y + j] = 1

print(sum(map(sum, board)))
