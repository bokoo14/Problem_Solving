# 2023.02.07
import sys
input = sys.stdin.readline

# 포도주를 2잔 연속까지는 마실 수 있음, 될 수 있는 대로 많은 양의 포도주를 맛보아야 함
n = int(input())
grape = [int(input()) for _ in range(n)]
dp=[0]*(n)
dp[0], dp[1] = grape[0], grape[0]+grape[1]
for i in range(2, n):
    dp[i]=max(dp[i-2], dp[i-1])+grape[i]

print(dp[n-1])