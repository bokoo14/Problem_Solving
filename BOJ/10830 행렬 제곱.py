# 2023.01.21
import sys
input = sys.stdin.readline

n, b = map(int, input().split()) # nXn행렬, A^b행렬 구하기
A = [list(map(int, input().split())) for _ in range(n)]

# 행렬의 곱
def multi(A, B):
    mulA=[[0]*(n) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                mulA[i][j]+=(A[i][k]*B[k][j])
            mulA[i][j]%=1000
    return mulA

# divide and conquer
def divideConquer(b, A):
    if b==1:
        for i in range(n):
            for j in range(n):
                A[i][j]%=1000
        return A
    elif b%2==0:
        B = divideConquer(b//2, A)
        return multi(B, B)
    elif b%2==1:
        B = divideConquer(b//2, A)
        return multi(A, multi(B, B))

answer=divideConquer(b, A)
for i in range(n):
    print(*answer[i])
