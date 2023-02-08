# 2023.02.08
import sys
input = sys.stdin.readline

A = list(ord(a)-65 for a in input().rstrip())
B = list(ord(b)-65 for b in input().rstrip())

dp = list([0]*(len(B)+1) for _ in range(len(A)+1))
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1]==B[j-1]: # 모두의 부분 수열이 되는 것이 있다면
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)][len(B)])