# attendeance = []
# for _ in range(28):
#     attendeance.append(int(input()))

# for i in range(1, 31):
#     if i not in attendeance:
#         print(i)

# v2

attendeance = list(range(1, 31))
for _ in range(28):
    attendeance.remove(int(input()))
print("\n".join(map(str, attendeance)))
