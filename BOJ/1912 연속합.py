#1912 연속합
#2022.08.18
#dp
import sys
input=sys.stdin.readline

n=int(input())
number=list(map(int, input().split()))

dp=[number[0]]*(n)

for i in range(0, n-1):
    dp[i+1]=max(dp[i]+number[i+1], number[i+1])
    

print(max(dp))

'''
for i in range(n):
    for j in range(i):
        ss=sum(number[j:i])
        dp[i]=max(ss, dp[i])
'''
