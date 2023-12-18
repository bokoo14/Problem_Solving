import sys
input = sys.stdin.readline

n = int(input())
find = []
for i in range(n):
    find.append(int(input()))

stack = [] # 임의의 스택
number = [i for i in range(1, n+1)] # 1~n까지의 수 => 스택에 넣었다 뺴면서 원하는 수열을 완성할 수 있는지 check
answer=[]
plusminus=[]
index=0
while number:
    stack.append(number.pop(0)) # 일단 스택에 넣음 -> +
    plusminus.append("+")
    while stack and stack[-1]==find[index]:
        index+=1
        answer.append(stack.pop()) # 스택의 제일 위의 값이 찾는 값과 일치 -> -
        plusminus.append("-")


while stack:
    answer.append(stack.pop()) # 스택에서 뻄 -> +
    plusminus.append("-")

if find == answer:
    for i in plusminus:
        print(i)
else:
    print("NO")
    