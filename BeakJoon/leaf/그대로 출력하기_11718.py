# https://www.acmicpc.net/problem/11718
# v1
while True:
    try:
        print(input())
    except EOFError:
        break

# v2
# print(open(0).read())
