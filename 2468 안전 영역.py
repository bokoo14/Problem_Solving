# 2023.01.25
import sys
input=sys.stdin.readline
from collections import deque

n = int(input())
graph=[]
maxDepth = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    maxDepth = max(maxDepth, max(graph[i])) # 물이 찰 수 있는 최대 높이

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(row, col, maxNum, visited):
    queue = deque()
    queue.append([row, col])
    visited[row][col]=True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<n:
                # maxNum보다 높고, 방문하지 않아야 함
                if graph[nx][ny]>maxNum and not visited[nx][ny]:
                    visited[nx][ny]=True
                    queue.append([nx, ny])

answer = 0
# 0~최대로 찰 수 있는 물의 높이까지
for i in range(maxDepth):
    visited=[[False]*(n) for _ in range(n)] # 방문 여부 
    area=0
    for r in range(n):
        for c in range(n):
            # 물의 높이보다 높고 방문하지 않았다면 새로운 안전한 영역
            if graph[r][c]>i and not visited[r][c]:
                bfs(r, c, i, visited)
                area+=1
    answer = max(answer, area)

print(answer)