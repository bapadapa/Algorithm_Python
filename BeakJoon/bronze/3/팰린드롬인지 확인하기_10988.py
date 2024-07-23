# v1
# s = input()
# flag = True
# for i in range(len(s)):
#     if s[i] != s[-i - 1]:
#         print(0)
#         flag = False
#         break
# if flag:
#     print(1)

# v2
s = input()
print(+(s[::-1] == s))
