# https://www.acmicpc.net/problem/11050
# n개의 집합에서 k개를 순서 없이 뽑은 조합의 가짓수
# e.g n:3,k:2 : (1,2), (1,3), (2,3) : 3
# 공식 : n! *((n-k)! * k!)
import sys


# for문
# def f(n):
#     ans = 1
#     for i in range(2, n + 1):
#         ans *= i
#     return ans
# 제귀
def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n - 1)


n, k = map(int, sys.stdin.readline().split())
print(f(n) // (f(n - k) * f(k)))
