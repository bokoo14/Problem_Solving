#2164
#2022.06.28

#덱을 이용
import sys
from collections import deque

N = int(sys.stdin.readline())

cards=deque()
for i in range(0, N):
    cards.append(i+1)
    

while len(cards)>1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])

'''
#리스트로 구현하면 시간초과
for i in range(0, N-1):
    del cards[0]
    pick=cards[0]
    del cards[0]
    cards.append(pick)

print(cards[0])

#큐로 구현하면 시간초과
while len(cards)>1:
    cards.pop(0)
    pick=cards.pop(0)
    cards.append(pick)


print(cards[0])
'''
