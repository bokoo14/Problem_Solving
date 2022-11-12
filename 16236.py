#16236 아기상어
#2022.08.03

'''
정렬-> 가장 윗쪽, 가장 왼쪽으로 우선순위 설정

'''
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
shark=[list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if shark[i][j]==9:
            location_X=i
            location_Y=j

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
size=2
def bfs(x, y, shark_size):
    distance=[[0]*(N) for _ in range(N)]
    visited=[[False]*(N) for _ in range(N)]
    temp=[]
    
    visited[x][y]=True
    queue=deque()
    queue.append([x, y])
    
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if shark[nx][ny]<=shark_size:
                    queue.append([nx, ny])
                    visited[nx][ny]=True
                    distance[nx][ny]=distance[a][b]+1
                    if shark[nx][ny]<shark_size and shark[nx][ny]!=0:
                        temp.append((nx, ny, distance[nx][ny]))

    #갈 수 있는 물고기 여러마리->가장 위쪽, 가장 왼쪽에 있는 물고기
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


eated_Fish=0
answer=0
while True:
    result=bfs(location_X, location_Y, size)

    if len(result)==0:
        break

    nx, ny, dist=result.pop()

    answer+=dist
    shark[x][y], shark[nx][ny]=0, 0

    location_X, location_Y = nx, ny
    eated_Fish+=1

    if eated_Fish==size:
        eated_Fish=0
        size+=1

print(answer)




















    
                
