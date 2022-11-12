#10828
#2022.06.29

#파이썬은 스택을 제공하지 않아서 list로 구현

import sys

N=int(sys.stdin.readline())

stack=[]
for i in range(0, N):
    command=sys.stdin.readline().split()
    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0]=='size':
        print(len(stack))
    elif command[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
    

      
