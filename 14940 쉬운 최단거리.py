# 2023.11.26

import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
"""
0: 원래 갈 수 없는 땅
1: 갈 수 있는 땅
2: 목표 지점
"""
visited = [[-1] * (m) for _ in range(n)] # 방문 여부
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = [[0] * (m) for _ in range(n)] # 목표 지점까지의 거리

def bfs(i, j): # breadth first search 너비우선탐색
    queue = deque()  # 덱으로 선언
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 그래프의 범위 내에 있고, 방문하지 않았고, 갈 수 있는 땅이라면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 1:
                visited[nx][ny] = 1  # 그래프 방문
                queue.append((nx, ny))
                answer[nx][ny] = answer[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == -1: # 원래 갈 수 있는 땅인 부분 중 도달할 수 없는 위치
            print("-1", end = " ")
        else:
            print(answer[i][j], end = " ")
    print()