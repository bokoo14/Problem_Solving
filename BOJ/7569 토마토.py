# 2023.01.09
import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
tomato=[[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

queue=deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==1:
                queue.append([i, j, k])

# 저장될 떄부터 모든 토마토가 익어있는 상태이면 0을 출력
if len(queue)==(m*n*h):
    print(0)
    exit(0)

# 토마토가 익어갈 방향: 6방향
dx=[-1, 1, 0, 0, 0, 0]
dy=[0, 0, -1, 1, 0, 0]
dz=[0, 0, 0, 0, -1, 1]
def bfs():
    while queue:
        x, y, z= queue.popleft()
        for i in range(6):
            nx=x+dx[i]
            ny=y+dy[i]
            nz=z+dz[i]
            # 다음에 이동할 곳이 범위를 벗어나지 않고, 익지 않은 토마토라면?
            if 0<=nx<h and 0<=ny<n and 0<=nz<m and tomato[nx][ny][nz]==0:
                tomato[nx][ny][nz]=tomato[x][y][z]+1
                queue.append([nx, ny, nz])

bfs()
answer=0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k]==0: # 토마토 모두가 익지 못하는 상황이라면
                print(-1)
                exit(0)
            answer=max(answer, tomato[i][j][k])

print(answer-1)            
