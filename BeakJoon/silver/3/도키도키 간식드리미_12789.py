# https://www.acmicpc.net/problem/12789
import sys

data = sys.stdin.readlines()

line = map(int, data[1].split())
waiting_line = []
num = 1

for student in line:
    # 줄서있는 학생들을 대기열로 넘김
    waiting_line.append(student)
    # 대기열에 줄서있는 학상들을 순서대로 배식
    while waiting_line and waiting_line[-1] == num:
        waiting_line.pop()
        num += 1
print("Sad" if waiting_line else "Nice")
