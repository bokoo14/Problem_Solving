#9461
#2022.07.09
'''
dp
규칙 찾기
'''
import sys

T=int(sys.stdin.readline())

for i in range(T):
    N=int(sys.stdin.readline())
    dp=[0]*(10000)

    dp[1]=1
    dp[2]=1
    dp[3]=1

    for i in range(4, N+1):
        dp[i]=dp[i-3]+dp[i-2]


    print(dp[N])
    
