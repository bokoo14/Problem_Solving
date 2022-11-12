#11047
#2022.06.30

import sys

N, M= map(int, sys.stdin.readline().split())

coin=[]
for i in range(0, N):
    coin.append(int(sys.stdin.readline()))

coin.reverse()
result=0
for i in range(0, N):
    if M//coin[i]>0:
        result+=M//coin[i]
        M=M%coin[i]


print(result)

