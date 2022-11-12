#2225 합분해
#2022.08.19
#dp
import sys
input = sys.stdin.readline

#0~N까지의 정수, K개를 더하기
N, K = map(int, input().split())

dp=[0]*(N+1)
dp[0]=1

for i in range(1, K+1):
    for j in range(1, N+1):
        dp[j]=()

'''
#중복조합
import sys

n,m=map(int,sys.stdin.readline().split())

def factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result

print((factorial(n+m-1)//(factorial(m-1)*factorial(n)))%1000000000)
'''
