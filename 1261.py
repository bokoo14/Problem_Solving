#1261 알고스팟
#2022.08.04

import sys
input=sys.stdin.readline
from collections import deque

M, N = map(int, input().split()) #열, 행
spot=[list(map(int, input().strip())) for _ in range(N)]

#이동할 수 있는 방향
dx=[1, 0, -1, 0]
dy=[0, 1, 0, -1]
visited=[[0]*(M) for _ in range(N)]

def bfs(x, y):
    global wallBreak
    queue=deque()
    queue.append([x, y])
    
    while queue:
        a, b = queue.popleft()
        if a==N-1 and b==M-1:
            print(spot[N-1][M-1])
            return

        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if spot[nx][ny]==0 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    spot[nx][ny]=spot[a][b] 
                    queue.appendleft([nx, ny])
                elif spot[nx][ny]==1 and visited[nx][ny]==0:
                    visited[nx][ny]=1
                    spot[nx][ny]=spot[a][b]+1
                    queue.append([nx, ny])

bfs(0, 0)

                    
