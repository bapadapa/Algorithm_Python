# https://www.acmicpc.net/problem/11653
num = int(input())
div = 2
while num != 1:
    if num % div == 0:
        print(div)
        num = num // div
    else:
        div += 1
