#16948
#2022.08.01

import sys
from collections import deque

N=int(sys.stdin.readline())
r1, c1, r2, c2=map(int, sys.stdin.readline().split())

dx=[-2, -2, 0, 0, 2, 2]
dy=[-1, 1, -2, 2, -1, 1]
chess=[[0]*(N) for _ in range(N)]
def bfs(x, y):
    queue=deque()
    queue.append((x, y))

    while queue:
        a, b=queue.popleft()
        if a==r2 and b==c2:
            return chess[r2][c2]

        for i in range(6):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<N and chess[nx][ny]==0:
                chess[nx][ny]=chess[a][b]+1
                queue.append((nx, ny))

    return -1


print(bfs(r1, c1))
