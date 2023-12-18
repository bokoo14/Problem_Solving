#1182
#2022.07.28
'''
브루트포스, 백트레킹
'''
'''
#브루트포스, 조합 이용해서 문제를 푸는 방법
#num에서 숫자를 1개~N+1개를 뽑아서 그 조합의 합이 S와 일치하면 cnt+=1
import sys
from itertools import combinations

#정수의 수, 합
N, S = map(int, sys.stdin.readline().split())
num=list(map(int, sys.stdin.readline().split()))

cnt=0
for i in range(1, N+1):
    com=list(combinations(num, i))

    comsum=0

    for c in com:
        if sum(c)==S:
            cnt+=1
            
print(cnt)
'''
'''
#브루트포스, 재귀를 이용하여 문제를 푸는 방식
import sys

N, S = map(int, sys.stdin.readline().split())
num=list(map(int, sys.stdin.readline().split()))
cnt=0

def subset(index, s):
    global cnt
    
    if index>=N:
        return
    
    s+=num[index]
    
    if s==S:
        cnt+=1

    subset(index+1, s) #선택 O
    subset(index+1, s-num[index]) #선택 X


subset(0,0)
print(cnt)
'''
    
