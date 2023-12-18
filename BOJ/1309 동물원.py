# 2023.02.03
import sys
input = sys.stdin.readline

n = int(input())

answer=0
dp=[[0]*(n+1) for _ in range(3)] # 경우의 수를 저장
dp[0][1]=1 # 모두 선택하지 않는 경우
dp[1][1]=1 # 1행을 선택하는 경우
dp[2][1]=1 # 2행을 선택하는 경우
for i in range(2,n+1): #col을 +1씩 이동
    # 현재 아무것도 선택하지 않았다면 그 전에는 (아무것도 선택하지 않음, 1행 선택, 2행 선택)->3가지 경우 모두 가능
    dp[0][i]=(dp[0][i-1]+dp[1][i-1]+dp[2][i-1])%9901 
    dp[1][i]=(dp[0][i-1]+dp[2][i-1])%9901
    dp[2][i]=(dp[0][i-1]+dp[1][i-1])%9901

print((dp[0][n]+dp[1][n]+dp[2][n])%9901)