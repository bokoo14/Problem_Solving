#9095
#2022.07.08
'''
dp로 풀기
규칙 찾기
'''

import sys

n=int(sys.stdin.readline())

for k in range(n):
    num=int(sys.stdin.readline())
    dp=[0]*(100000)
    dp[1]=1
    dp[2]=2
    dp[3]=4
    for i in range(4, num+1):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

    print(dp[num])
