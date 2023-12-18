# 2023.01.15
import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

Adic=defaultdict(int)
Bdic=defaultdict(int)
for i in range(n):
    for j in range(i, n):
        Adic[sum(A[i:j+1])]+=1
for i in range(m):
    for j in range(i, m):
        Bdic[sum(B[i:j+1])]+=1

answer=0
for psum in Adic.keys():
    answer+=Adic[psum]*Bdic[t-psum]
print(answer)
