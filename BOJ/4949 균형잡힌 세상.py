#2023.01.03
import sys
input = sys.stdin.readline

while(1):
    word = input().rstrip()
    if word=='.':
        break
    
    answer=0 
    stack=[]
    for i in word:
        if i=="(" or i=="[":
            stack.append(i)
        elif i==")":
            if len(stack)==0:
                answer=1
                break
            elif stack[-1]!="(":
                answer=1
                break
            else:
                stack.pop()
        elif i=="]":
            if len(stack)==0:
                answer=1
                break
            elif stack[-1]!="[":
                answer=1
                break
            else:
                stack.pop()
                
    if answer==0 and len(stack)==0:
        print("yes")
    else:
        print("no")
    


