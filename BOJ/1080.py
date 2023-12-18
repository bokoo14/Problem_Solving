#1080 행렬
#2022.08.08

import sys
input=sys.stdin.readline

N, M = map(int, input().split())
A=[list(map(int, input().strip())) for _ in range(N)]
B=[list(map(int, input().strip())) for _ in range(N)]

cnt=0
for i in range(N-2):
    for j in range(M-2):
        if A[i][j]!=B[i][j]:
            for k in range(i, i+3):
                for p in range(j, j+3):
                    A[k][p]=1-A[k][p]
            cnt+=1
                    

                
#바꿀 수 없다면 -1출력                
for i in range(N):
    for j in range(M):
        if A[i][j]!=B[i][j]:
            print(-1)
            exit()


#바꾸었으면 정답 출력
print(cnt)
