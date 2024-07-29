# https://www.acmicpc.net/problem/1620

import sys

l = sys.stdin.readlines()
n, q = map(int, l[0].split())
document = {value: index + 1 for index, value in enumerate(l[1 : n + 1])}
for quiz in l[n + 1 :]:
    if quiz.strip().isdigit():
        print(document.get(quiz))
    else:
        print(document[quiz])
