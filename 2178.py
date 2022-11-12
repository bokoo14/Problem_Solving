#2178
#2022.07.26
'''
그래프 이론, 그래프 탐색, 너비 우선 탐색
'''

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
def bfs(x, y):
    queue=deque()
    queue.append((x, y))
    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=N or ny<0 or ny>=M:
                continue
            if maze[nx][ny]==0:
                continue
            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx, ny))

bfs(0, 0)
print(maze[N-1][M-1])
          
            
                
