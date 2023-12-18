#11047 동전0
#2022.08.10
import sys
input=sys.stdin.readline

N, K = map(int, input().split())

coin=[0]*(N)
for i in range(N):
    coin[i]=int(input())

cnt=0
for j in reversed(range(N)):
    if K//coin[j]>0:
        cnt+=(K//coin[j])
        K=K%coin[j]

print(cnt)
