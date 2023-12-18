# 2023.01.04
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 물품의 수, 최대 무게
item=[list(map(int, input().split())) for _ in range(n)]

dp=[[0]*(k+1) for _ in range(n+1)] # 행: 물품의 수, 열: 무게
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = item[i-1][0] # 무게
        value = item[i-1][1] # 가치

        if j<weight: # 현재의 무게보다 item의 무게가 더 크다면, 포함하지 않음
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[n][k])