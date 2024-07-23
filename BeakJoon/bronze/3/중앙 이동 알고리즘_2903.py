# https://www.acmicpc.net/problem/2903


# v1
# (기존 가로점 개수 + (기존 가로점 개수 - 1)) 로 점수가 늘어남
# 전체 개수를 구하려면 위 값에 2제곱을 해주면 됨
num = 2
for i in range(1, int(input()) + 1):
    num += num - 1
print(num**2)


# v2
# 2 - 3 - 5 - 9 - 17 - 33 - 65 - 129 - 257 - 513
# 위와 같이 늘어가는데 등차가 1+ 2**n 으로 늘어남
# 2 ** (n) + 1 을 제곱한 값
print((2 ** (int(input())) + 1) ** 2)
