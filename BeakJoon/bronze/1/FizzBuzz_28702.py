# https://www.acmicpc.net/problem/28702
import sys

data = sys.stdin.readlines()
idx = num = 0
# 다음수 구하기
for index, i in enumerate(data):
    is_digit = i.strip().isdigit()
    if is_digit:
        num = int(i)
        idx = index
        break
next_num = num + 3 - idx

if next_num % 3 == next_num % 5 == 0:
    print("FizzBuzz")
elif next_num % 3 == 0:
    print("Fizz")
elif next_num % 5 == 0:
    print("Buzz")
else:
    print(next_num)
