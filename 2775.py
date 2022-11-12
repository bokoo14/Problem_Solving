#2775
#2022.07.26

import sys

T=int(sys.stdin.readline())

for i in range(T):
    k=int(sys.stdin.readline())#층
    n=int(sys.stdin.readline())#호수
    apart=[[0]*(n+1) for _ in range(k+1)]

    for i in range(n+1):
        apart[0][i]=i

    for i in range(1, k+1):
        for j in range(1, n+1):
            s=0
            for p in range(1, j+1):
                s+=apart[i-1][p]
            apart[i][j]=s

    print(apart[k][n])
