# https://www.acmicpc.net/problem/1735
import sys

data = sys.stdin.readlines()

st = [int(x) for x in data[1:]]
length = st[-1] - st[0]

differences = [st[i + 1] - st[i] for i in range(len(st) - 1)]

min_len = min(differences)
max_len = max(differences)
gcd = max_len
for i in set(differences[1:]):
    a = min_len
    b = i
    tmp = 0
    while b:
        a, b = b, a % b
        tmp = a
    gcd = min(gcd, tmp)
print(int((length / gcd + 1) - int(data[0])))
