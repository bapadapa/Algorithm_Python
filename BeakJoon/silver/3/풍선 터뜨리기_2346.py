# https://www.acmicpc.net/problem/2346
import sys
from collections import deque

data = sys.stdin.readlines()

# 인덱스도 기록하기 위해 enumerate로 묶음
q = deque(enumerate(map(int, data[1].split())))

result = []
while q:
    idx, move = q.popleft()
    result.append(idx + 1)
    # 왼쪽으로 값만큼 이동
    # e.g rotate(1) : 1,2,3 ->  2,3,1
    q.rotate(-(move - 1) if move > 0 else -move)

print(" ".join(map(str, result)))
