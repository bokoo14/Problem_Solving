#10845
#2022.06.30

import sys

N=int(sys.stdin.readline())

queue=[]
for i in range(0, N):
    command=sys.stdin.readline().split()

    if command[0]=='push':
        queue.append(command[1])
    elif command[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.pop(0))
    elif command[0]=='size':
        print(len(queue))
    elif command[0]=='empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif command[0]=='back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[len(queue)-1])
            

