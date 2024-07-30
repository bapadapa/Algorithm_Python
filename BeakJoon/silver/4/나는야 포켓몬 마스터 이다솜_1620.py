# https://www.acmicpc.net/problem/1620

import sys

l = sys.stdin.readlines()
n, q = map(int, l[0].split())
document = {value[:-1]: index + 1 for index, value in enumerate(l[1 : n + 1])}
reversed_dict = {v: k for k, v in document.items()}
for quiz in l[n + 1 :]:
    quiz = quiz[:-1]
    if quiz.isdigit():
        print(reversed_dict.get(int(quiz)))
    else:
        print(document.get(quiz))
