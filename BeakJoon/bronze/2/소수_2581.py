# https://www.acmicpc.net/problem/2581

start = int(input())
end = int(input())

prime_num = []
prime_min_num = -1
for i in range(start, end + 1):
    is_prime = 0
    for j in range(i)[1:]:
        if i % j == 0:
            is_prime += 1
        if is_prime > 1:
            break
    if is_prime == 1:
        prime_num.append(i)
        prime_min_num = i if prime_min_num == -1 else prime_min_num

if prime_min_num != -1:
    print(sum(prime_num))
print(prime_min_num)
