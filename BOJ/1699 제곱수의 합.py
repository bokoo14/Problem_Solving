import sys
input = sys.stdin.readline

n = int(input())
dp=[i for i in range(n+1)]
# dp table에 최소 개수를 저장
for i in range(1, n+1):
    for j in range(1, i): # 현재 dp의 index에 넣을 값
        if j*j>i: # 제곱수가 안되면
            break
        if dp[i]>dp[i-j*j]+1: # 현재 저장된 값보다 check하는 값이 더 작으면 갱신
            dp[i]=dp[i-j*j]+1 

print(dp[-1])