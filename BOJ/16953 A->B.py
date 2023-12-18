# 2022.12.31
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 0

while (1):
    cnt+=1
    tmp = b

    if a==b:
        print(cnt)
        break
    if b%10==1:
        b//=10
    elif b%2==0:
        b//=2
        
    if tmp ==b:
        print("-1")
        break