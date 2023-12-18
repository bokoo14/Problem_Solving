# 2023.07.04
import sys

input = sys.stdin.readline

n = int(input())
card = [0] + list(map(int, input().split()))

dp = [10001] * (n + 1)
dp[0] = card[0]

for i in range(n + 1):
    for j in range(1, i + 1):  # 0~i까지 진행
        dp[i] = min(dp[i - j] + card[j], dp[i])

print(dp[n])
