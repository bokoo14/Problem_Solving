# 2023.01.29
import sys
input = sys.stdin.readline

n = int(input())
card = [0]+list(map(int, input().split()))
dp=[0]*(n+1) # index: 카드팩의 수, value:지불해야 하는 금액

for i in range(1, n+1): # dp
    for j in range(1, i+1): # card
        if i-j>=0:
            dp[i]=max(dp[i], dp[i-j]+card[j]) # 해당하는 카드를 선택 O or X

print(dp[n])