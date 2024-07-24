# https://www.acmicpc.net/problem/14215
# v1
lengths = sum(sticks := list(map(int, input().split())))
maxLen = max(sticks)
if len({*sticks}) == 1:
    print(lengths)
elif lengths <= maxLen * 2:
    sticks.remove(maxLen)
    restStick = sum(sticks)
    print(restStick + min(maxLen, restStick - 1))
else:
    print(lengths)

# v2
# lengths <= maxLen * 2 조건이 불필요
lengths = sum(sticks := list(map(int, input().split())))
maxLen = max(sticks)
if len({*sticks}) == 1:
    print(lengths)
else:
    sticks.remove(maxLen)
    restStick = sum(sticks)
    print(restStick + min(maxLen, restStick - 1))
