#14888
#2022.07.27

import sys
from itertools import permutations

N=int(sys.stdin.readline())
A=list(map(int, sys.stdin.readline().split()))
B= list(map(int, sys.stdin.readline().split()))
opera=['+','-','*','/']

op=[]

for i in range(len(B)):
    for j in range(B[i]):
        op.append(opera[i])

answer=[]
for operation in list(permutations(op, N-1)):
    count=A[0]
    for i in range(1, N):
        if operation[i-1]=='+':
            count+=A[i]
        elif operation[i-1]=='-':
            count-=A[i]
        elif operation[i-1]=='*':
            count*=A[i]
        elif operation[i-1]=='/':
            count=int(count/A[i])

    answer.append(count)


print(max(answer))
print(min(answer))

