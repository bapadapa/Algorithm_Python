# https://www.acmicpc.net/problem/10250
import sys

data = sys.stdin.readlines()

for i in data[1:]:
    h, w, n = map(int, i.split())
    room = n // h
    floor = n % h
    is_zero = floor == 0
    print((h if is_zero else floor) * 100 + (room if is_zero else room + 1))
