#9012
#2022.07.08

import sys

n=int(sys.stdin.readline())

for i in range(0, n):
    ss=sys.stdin.readline().strip()
    ss=list(ss)
    test=[]
    for j in range(0, len(ss)):
        if ss[j]=='(':
            test.append('(')
        elif ss[j]==')':
            if len(test)==0:
                print("No")
                break
            else:
                test.pop()
                

    else:
        if len(test)==0:
            print("Yes")
        else:
            print("No")



'''
T = int(input())

for i in range(T):
    stack = []
    a=input()
    for j in a:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호가 없을경우 NO
                print("NO")
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다
        if not stack: # break문으로 안끊기고 스택이 비어있다면 괄호가 다 맞는거다.
            print("YES")
        else: # break안 걸렸더라도 스택에 괄호가 들어있다면 NO이다.
            print("NO")
'''

