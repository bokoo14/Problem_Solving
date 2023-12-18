#7576
#2022.08.01
#너비 우선 탐색

import sys
from collections import deque

#열, 행
M, N = map(int, sys.stdin.readline().split())
tomato=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

#1일때만 덱에 넣어줌
queue=deque()
for i in range(N): #행
    for j in range(M): #열
        if tomato[i][j]==1:
            queue.append([i, j])

def bfs():
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<M and tomato[nx][ny]==0:
                tomato[nx][ny]=tomato[a][b]+1
                queue.append([nx, ny])
                
bfs()
answer=0
for i in range(N):
    for j in range(M):
        if tomato[i][j]==0:
            print(-1)
            exit(0)
        answer=max(answer, tomato[i][j])

print(answer-1)
