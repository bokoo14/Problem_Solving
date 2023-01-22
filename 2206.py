#2206
#2022.07.30

#그래프 탐색, 너비 우선 탐색
'''
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
wall=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]


breakmove=False
visited=[[0]*(M) for _ in range(N)] #방문 여부
distance=[[0]*(M) for _ in range(N)] #경로의 길이
distance[0][0]=1
def bfs(x, y):
    global breakmove
    
    queue=deque() #덱 생성
    queue.append((x, y))

    while queue:
        a, b=queue.popleft()
        if a==N-1 and b==M-1:
            return distance[N-1][M-1]

        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<M:
                #벽이고 깬 적이 없고 방문한 적이 없을 때
                if wall[nx][ny]==1 and breakmove==False:
                    breakmove=True
                    distance[nx][ny]=distance[a][b]+1
                    queue.append((nx, ny))
                #벽이 아니고 방문한 적이 없을 때
                elif wall[nx][ny]==0 and visited[nx][ny]==0:
                    distance[nx][ny]=distance[a][b]+1
                    queue.append((nx, ny))

    return -1 #불가능할 때는 -1
                    

print(bfs(0, 0))
'''       
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
wall=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

#3차원 배열
#visited[][][0]: 벽을 부수지 않은 경우
#visited[][][1]: 벽을 부순 경우
distance=[[[0]*2 for _ in range(M)] for _ in range(N)]
distance[0][0][0]=1

def bfs(x, y, z):
    queue=deque() #덱 생성
    queue.append((x, y, z))

    while queue:
        a, b, c=queue.popleft()
        if a==N-1 and b==M-1:
            return distance[a][b][c]

        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<N and 0<=ny<M:
                #벽을 부수는 경우
                #벽을 부수면 distance[][][1]로 계속 계산해줘야 함
                if wall[nx][ny]==1 and c==0:
                    distance[nx][ny][1]=distance[a][b][0]+1 
                    queue.append((nx, ny, 1))
                #벽이 아닌 경우
                elif wall[nx][ny]==0 and distance[nx][ny][c]==0:
                    distance[nx][ny][c]=distance[a][b][c]+1
                    queue.append((nx, ny, c))

    return -1 #불가능할 때는 -1
                    
print(bfs(0, 0, 0))       
        
    
