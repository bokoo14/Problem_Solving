# 2023.01.18
import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

sumA = defaultdict(int)
sumB = defaultdict(int)
for i in range(n):
    for j in range(i, n):
        sumA[sum(A[i:j+1])]+=1
for i in range(m):
    for j in range(i, m):
        sumB[sum(B[i:j+1])]+=1

answer=0
for a in sumA.keys():
    answer+=(sumA[a]*sumB[t-a])
print(answer)