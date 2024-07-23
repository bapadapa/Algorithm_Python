# https://www.acmicpc.net/problem/1978
cnt = 0
_ = input()
for num in map(int, input().split()):
    check_prime = 0
    for i in range(num)[1:]:
        if num % i == 0:
            check_prime += 1
        if check_prime > 2:
            break
    cnt += 1 if check_prime == 1 else 0
print(cnt)
