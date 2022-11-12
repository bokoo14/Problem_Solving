#15989 123더히기4
#2022.08.19
import sys
input = sys.stdin.readline

T= int(input())

for i in range(T):
    n=int(input())
    dp=[0]*(n+3)
    dp[1]=1
    dp[2]=2
    dp[3]=3
    for j in range(4, n+3):
        dp[j]=dp[j-1]+(dp[j-2]-dp[j-3])

        if j%3==0:
            dp[j]+=1

    print(dp[n])

