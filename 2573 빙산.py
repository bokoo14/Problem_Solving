# 2023.01.28
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

ice=[]
for i in range(n):
    for j in range(m):
        if graph[i][j]!=0: # 빙하라면 ice에 append
            ice.append((i,j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, visited):
    q = deque([[x, y]])
    visited[x][y]=True
    meltList=[]
    while q:
        melt=0 # 상하좌우 중에 물인 경우 melt+=1
        a, b = q.popleft() # 현재 위치에 해당하는 빙하
        for i in range(4):
            nx = dx[i]+a
            ny = dy[i]+b
            if 0<=nx<n and 0<=ny<m:
                if not graph[nx][ny]: # 상하좌우 물인 경우
                    melt+=1
                elif graph[nx][ny] and not visited[nx][ny]: # 상하좌우가 빙하이고 큐에 들어간 적이 없는 경우
                    q.append([nx, ny])
                    visited[nx][ny]=True
        if melt>0: #한번이상 녹아야 한다면: 현재 위치 & 녹을 빙하의 깊이
            meltList.append([a, b, melt])
    # 큐(빙하의 리스트들)를 모두 탐색하였다면: 녹여줘야 할 빙하를 녹여야 함
    for meltX, meltY, meltD in meltList:
        graph[meltX][meltY]=max(0, graph[meltX][meltY]-meltD)

    return 1

year=0 # 빙산이 분리되는 최초의 시간(년)
while ice: # 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력
    visited = [[False]*(m) for _ in range(n)] # 방문 여부 check
    group=0
    allMelted =[] # 모두 녹아서 ice에서 제거해야 할 리스트
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]: # 빙산 & 방문하지 않았다면?
                group+=bfs(i, j, visited)
            if not graph[i][j] and visited[i][j]: # 그래프 탐색 후, 원래는 빙산이었지만 모두 녹아 물이 되었다면
                allMelted.append((i, j))

    if group>=2: # 빙산이 두 덩어리 이상으로 분리된다면?
        print(year)
        break
    year+=1
    ice = list(set(ice)-set(allMelted))
else:
    print(0)