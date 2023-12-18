#10026
#2022.08.01

import sys
from collections import deque

N= int(sys.stdin.readline())
redgreen=[list(map(str, sys.stdin.readline().strip())) for _ in range(N)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
visited=[[0]*(N) for _ in range(N)]

def bfs(x, y):
    queue=deque()
    queue.append([x, y])

    while queue:
        a, b=queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if redgreen[nx][ny]==redgreen[a][b]:
                    visited[nx][ny]=1
                    queue.append([nx, ny])
    return

#적록색약이 아닐때
no_cnt=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            no_cnt+=1
            bfs(i, j)


#적록색약일때
visited=[[0]*(N) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if redgreen[i][j]=='R':
            redgreen[i][j]='G'

yes_cnt=0
for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            yes_cnt+=1
            bfs(i, j)

print(no_cnt, yes_cnt)

