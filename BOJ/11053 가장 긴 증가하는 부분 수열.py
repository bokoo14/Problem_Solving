#11053 가장 긴 증가하는 부분 수열
#2022.08.12
#dp
import sys
input=sys.stdin.readline

N = int(input())
array=list(map(int, input().split()))

dp=[1]*(N)
for i in range(N):
    for j in range(i):
        if array[i]>array[j]:
            dp[i]=max(dp[i], dp[j]+1)
        
print(max(dp))
