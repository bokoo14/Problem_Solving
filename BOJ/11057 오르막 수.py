# 2023.01.28
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# A<=A<=A ... <=A -> 10개 중에 중복을 허락하여 n개를 뽑으면 된다!
# (10)H(n) = (10+n-1)C(n) = (9+n)!//(n!)//(9!) 
n = int(input()) # 수의 길이

def com(n):
    if n==1:
        return 1
    return n*com(n-1)

answer = com(9+n)//com(n)//com(9)%10007
print(answer)