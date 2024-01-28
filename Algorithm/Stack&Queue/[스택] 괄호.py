import sys
input =sys.stdin.readline

# 뒤에 붙이는건 ")" 스택에 남아있는 갯수"("만큼 붙여주면 된다 len(stack)
# 앞에 붙이는건 "(" close를 만나면 pop을 시켜줘야 하는데 스택이 비어있으면 +1만큼 증가시켜준다

def sol(array):
    cnt = 0
    stack=[]
    for i in range(len(array)):
        if array[i]=="(":
            stack.append(array[i])
        else:
            if len(stack)==0:
                cnt+=1
            else:
                stack.pop()
                
    return cnt+len(stack)

array = list(input().strip())
print(sol(array))

