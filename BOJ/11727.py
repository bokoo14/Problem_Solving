#11727
#2022.07.09

import sys

n=int(sys.stdin.readline())

dp=[0]*(100000)

dp[1]=1
dp[2]=3
dp[3]=5
dp[4]=11

for i in range(5, n+1):
    dp[i]=2*dp[i-2]+dp[i-1]

print(dp[n]%10007)

