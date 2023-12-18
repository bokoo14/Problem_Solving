# 2023.01.01
import sys
input = sys.stdin.readline

n = int(input())
RGB = [list(map(int, input().split())) for _ in range(n)]

dp=[[0]*(n) for _ in range(n)]
dp[0][0]=RGB[0][0] #red
dp[0][1]=RGB[0][1] #green
dp[0][2]=RGB[0][2] #blue

for i in range(1, n):
    dp[i][0]=min(dp[i-1][1], dp[i-1][2])+RGB[i][0] #red -> 이전: green or blue
    dp[i][1]=min(dp[i-1][0], dp[i-1][2])+RGB[i][1] #green -> 이전: red or blue
    dp[i][2]=min(dp[i-1][0], dp[i-1][1])+RGB[i][2] #blue -> 이전: red or green


print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))

