# 킹, 퀸, 룩, 비숍, 나이트, 폰
# https://www.acmicpc.net/problem/3003

sets = [1, 1, 2, 2, 2, 8]
print(
    " ".join(
        map(str, [sets[i] - int(x) for i, x in enumerate(map(int, input().split()))])
    )
)
