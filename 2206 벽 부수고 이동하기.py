# 2023.01.21
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # nXm행렬
wall=[list(map(int, str(input().rstrip()))) for _ in range(n)]

# 이동 방향
dy = [1, -1, 0, 0] 
dz = [0, 0, 1, -1]
def bfs():
    distance=[[[0]*m for _ in range(n)] for _ in range(2)]
    distance[0][0][0]=1
    queue = deque()
    queue.append([0, 0, 0])
    while queue:
        x, y, z = queue.popleft() # 벽 뚫었는지(높이), 행, 열
        if y==n-1 and z==m-1:
            return distance[x][y][z]
        for i in range(4):
            ny=dy[i]+y
            nz=dz[i]+z
            if 0<=ny<n and 0<=nz<m:
                if wall[ny][nz]==1 and x==0: # 벽인 경우
                    distance[1][ny][nz]=distance[0][y][z]+1
                    queue.append([1, ny, nz])
                elif wall[ny][nz]==0 and distance[x][ny][nz]==0: # 그냥 지나가도 되는 경우
                    distance[x][ny][nz]=distance[x][y][z]+1
                    queue.append([x, ny, nz])
    return -1

print(bfs())
