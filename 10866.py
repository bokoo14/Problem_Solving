#10866
#2022.06.30

#popleft는 리스트에서 지원하지 않아서 deque를 썼다

import sys
from collections import deque

N=int(sys.stdin.readline())

deque=deque()
for i in range(0, N):
    command=sys.stdin.readline().split()

    if command[0]=='push_front':
        deque.insert(0, command[1])
    elif command[0]=='push_back':
        deque.append(command[1])
    elif command[0]=='pop_front':
        if len(deque)==0:
            print(-1)
        else:
            print(deque.popleft())
    elif command[0]=='pop_back':
        if len(deque)==0:
            print(-1)
        else:

            print(deque.pop())
    elif command[0]=='size':
        print(len(deque))
    elif command[0]=='empty':
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif command[0]=='back':
        if len(deque)==0:
            print(-1)
        else:
            print(deque[len(deque)-1])
            
