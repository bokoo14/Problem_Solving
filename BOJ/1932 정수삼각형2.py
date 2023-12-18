# 2023.01.04
import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(n-1, -1, -1): # 행
    for j in range(i): # 열
        triangle[i-1][j]+=(max(triangle[i][j], triangle[i][j+1]))

print(triangle[0][0]) 