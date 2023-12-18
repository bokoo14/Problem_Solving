# 2023.01.28
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
value = [int(input()) for _ in range(n)]

dp=[10**9]*(k+1) # 동전의 개수
dp[0]=0 # 0은 동전을 0개 선택함
for v in value: # 동전의 가치
    for index in range(v, k+1):
        if index>=v: 
            dp[index]=min(dp[index], dp[index-v]+1)

if dp[k]!=10**9:
    print(dp[k])
else:
    print(-1)