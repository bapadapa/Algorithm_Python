# https://www.acmicpc.net/problem/2164

from collections import deque

cards = deque([x for x in range(1, int(input()) + 1)])
while len(cards) != 1:
    print(cards)
    del cards[0]
    cards.append(cards.popleft())
print(cards[0])
