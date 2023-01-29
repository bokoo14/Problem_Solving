# 2023.01.29
import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*(2) for _ in range(n)]

dp[0][0], dp[0][1]= 0, 1
for i in range(1, n):
    for j in range(2):
        if j==0:
            dp[i][j]=dp[i-1][0]+dp[i-1][1]
        else:
            dp[i][j]=dp[i-1][0]
print(dp[n-1][0]+dp[n-1][1])