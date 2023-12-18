#10773
#2022.06.28

import sys
from collections import deque

K=int(sys.stdin.readline())

number=deque()
store=deque()
total=0
compare=0

#스택과 큐 활용
for i in range(0, K):
    number.append(int(sys.stdin.readline()))

store=number

for i in range(0, K):
    compare=number.popleft()
    if compare==0:
        store.pop()
    else:
        store.append(compare)

for i in range(0, len(store)):
    total+=store.pop()
        
print(total)
