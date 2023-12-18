#2667
#2022.07.29
'''
그래프, 깊이  우선 탐색
덱을 이용하여 너비 우선 탐색으로도 풀 수 있음
'''
import sys

N=int(sys.stdin.readline())
home=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited=[[False]*(N) for _ in range(N)]
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def dfs(x, y):
    global cnt
    visited[x][y]=True
    if home[x][y]==1:
        cnt+=1
        
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<N and home[nx][ny]==1 and visited[nx][ny]==False:
            dfs(nx, ny)
            
cnt=0
answer=[]
for i in range(N):
    for j in range(N):
        if home[i][j]==1 and visited[i][j]==False:
            dfs(i, j)
            answer.append(cnt)
            cnt=0

print(len(answer))
for i in sorted(answer):
    print(i)
            

