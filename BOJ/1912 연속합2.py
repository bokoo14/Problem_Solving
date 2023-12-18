# 2023.01.04
import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))

dp = [0]*(n)
dp[0]=number[0]

for i in range(1, n):
    dp[i]+=(max(dp[i-1], 0)+number[i])

print(max(dp))