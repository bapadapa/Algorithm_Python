# https://www.acmicpc.net/problem/2750

l = []

for _ in range(int(input())) :
    l.append(int(input()))
l.sort()

print(*l ,sep='\n')

for i in l :
    print(i)