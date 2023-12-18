#5525
#2022.08.01

import sys

N = int(sys.stdin.readline()) #몇번째인지 
M = int(sys.stdin.readline()) #문자열의 길이
S=sys.stdin.readline().strip()

N_Count=0
answer=0
i=0
while i<M-1:
    if S[i:i+3]=='IOI':
        i+=2
        N_Count+=1
        if N_Count==N:
            answer+=1
            N_Count-=1
    else:
        i+=1
        N_Count=0

print(answer)


'''
서브 테스크2를 통과하지 못함
서브 테스크 1: input의 길이가 짧기 때문에 100*10000으로 통과할 수 있음
서브 테스크 2: O(N), O(NlogN)의 시간 복잡도를 가지게 해야 함
단일 for문을 이용하여 구현-> 단순 비교가 아니라 연산을 통해 문자열 찾기
'''       
'''
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S=list(sys.stdin.readline().strip())

cnt=0
P=[0]*(N+1)
for i in range(N+1):
    s=''
    for j in range(i):
        s=s+'OI'
    P[i]='I'+s

a=len(P[N])
for i in range(M-a):
    compare=''
    for j in range(i, i+a):
        compare+=S[j]
    if compare==P[N]:
        cnt+=1

print(cnt)
'''
