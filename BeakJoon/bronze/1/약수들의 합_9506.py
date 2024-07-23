# https://www.acmicpc.net/problem/9506
nums = []
while True:
    num = int(input())
    if num == -1:
        break
    nums.append(num)
nums.sort()

for num in nums:
    num_list = []
    for i in range(num)[1:]:
        if num % i == 0:
            num_list.append(i)
    if sum(num_list) == num:
        print(f"{num} = {' + '.join(map(str, num_list))}")
    else:
        print(f"{num} is NOT perfect.")
