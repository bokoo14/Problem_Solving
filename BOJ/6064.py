#6064
#2022.08.02

import sys

T=int(sys.stdin.readline()) #테스트 데이터

for i in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    TF=False
    k=x
    while k<=M*N:
        if (k-x)%M==0 and (k-y)%N==0:
            print(k)
            TF=True
            break
        k+=M

    if TF==False:
        print(-1)

        
    
