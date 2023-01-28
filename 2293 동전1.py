# 2023.01.28
import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # n가지 종류,가치의 합 k원
value = [int(input()) for _ in range(n)]

dp=[0]*(k+1) # dp의 index: 가치의 합, value: 경우의 수
dp[0]=1 # 가치의 합이 0: 동전을 하나도 쓰지 않는 경우
for v in value:
    for index in range(1, k+1):
        if index>=v: # (해당하는 가치의 합-가치)>=0 : 이전의 가치의 합을 더해주면 됨
            dp[index]+=dp[index-v]
print(dp[k])