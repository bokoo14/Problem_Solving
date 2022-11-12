#1018
#2022.06.28

'''
브루트포스 알고리즘
'''

import sys

#행, 열
N, M= map(int, sys.stdin.readline().split())

check=[]
for i in range(N):
    check.append(sys.stdin.readline())


answer=[]
for i in range(0, N-7):
    for j in range(0, M-7):
        W=0
        B=0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2==0:
                    if check[k][l]=='B':
                        B+=1
                    if check[k][l]=='W':
                        W+=1
                else:
                    if check[k][l]=='B':
                        W+=1
                    if check[k][l]=='W':
                        B+=1
        answer.append(B)
        answer.append(W)


print(min(answer))
