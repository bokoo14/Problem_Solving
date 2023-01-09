# 2023.01.08
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())
for i in range(t):
    p=list(input().strip())
    n=int(input())
    if n==0:
        number=input()
        number=[]
    else:
        number=deque(input().strip()[1:-1].split(","))
    
    R=0
    answer=1
    for j in p:
        if j=='R': #  R=>뒤집어야 할때
            R+=1
        else: # W=>제일 첫번째 수를 버려야 할때 
            if len(number)==0:
                print("error")
                answer=0
                break
            elif R%2==1:
                number.pop()
            else:
                number.popleft()

    if answer==1 and R%2==0:
        print("["+",".join(number)+"]")
    elif answer==1 and R%2==1:
        number.reverse()
        print("["+",".join(number)+"]")
        