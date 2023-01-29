# 2023.01.29
import sys
input = sys.stdin.readline
n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n) for _ in range(n)] # 경우의 수
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            print(dp[i][j])
        nextRow = i+game[i][j]
        nextCol = j+game[i][j]
        if nextRow<n: # 다음으로 이동할 수 있다면
            dp[nextRow][j]+=dp[i][j]
        if nextCol<n:
            dp[i][nextCol]+=dp[i][j]