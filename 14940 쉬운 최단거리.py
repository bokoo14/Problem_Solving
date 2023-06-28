# 2023.06.27

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[-1]*m for _ in range(n)]

findingX, findingY = -1, -1
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            findingX, findingY = j, i
print(graph)
print(i, j)