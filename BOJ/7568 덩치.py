# 2023.01.02
import sys
input = sys.stdin.readline

n = int(input())
body = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    cnt=1
    for j in range(n):
        if body[i][0]<body[j][0] and body[i][1]<body[j][1]:
            cnt+=1
    print(cnt, end = " ")
