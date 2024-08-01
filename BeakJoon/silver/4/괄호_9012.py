# https://www.acmicpc.net/problem/9012
import sys

data = sys.stdin.readlines()

for i in data[1:]:
    cnt1 = 0
    cnt2 = 0
    for j in i[:-1]:
        if j == "(":
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt2 > cnt1:
            break
    print("YES" if cnt1 == cnt2 else "NO")
