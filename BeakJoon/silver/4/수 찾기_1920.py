# https://www.acmicpc.net/problem/1920
import sys

data = sys.stdin.readlines()

a = set(data[1].strip().split())
print("\n".join(["1" if num in a else "0" for num in data[3].split()]))
