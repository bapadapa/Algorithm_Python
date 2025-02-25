# https://www.acmicpc.net/problem/19532

a, b, c, d, e, f = map(int, input().split())
flag = True
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if( a*x + b*y == c and d*x + e*y == f):
            print(x,y)
            flag = False
            break
    if(flag == False):
        break