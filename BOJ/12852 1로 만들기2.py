# 2023.01.30
import sys
input = sys.stdin.readline

n = int(input())
dp=[[0]*(2) for _ in range(n+1)]  #연산을 하는 횟수의 최솟값
dp[1][0]=0 # 연산횟수
dp[1][1]=[1] # 연산순서

# n~1 dp table탐색
for i in range(2, n+1):
    dp[i][0]=dp[i-1][0]+1 # 연산횟수
    dp[i][1]=dp[i-1][1]+[i] # 연산순서
    if i%3==0 and dp[i//3][0]+1 < dp[i][0]: # 3으로 나눌 수 있고, 연산횟수가 더 작으면 
        dp[i][0]=dp[i//3][0]+1
        dp[i][1]=dp[i//3][1]+[i]
    if i%2==0 and dp[i//2][0]+1 < dp[i][0]: # 2로 나눌 수 있고, 연산 횟수가 더 작으면
        dp[i][0]=dp[i//2][0]+1
        dp[i][1]=dp[i//2][1]+[i]
print(dp[n][0])
print(*reversed(dp[n][1]))
