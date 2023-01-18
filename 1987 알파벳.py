# 2023.01.18
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
alpha = [list(input().rstrip()) for _ in range(r)]

visited=[0]*(26) # 26개의 알파벳을 방문했는지 check
visited[ord(alpha[0][0])-65]=1 # 0행 0열의 알파벳 방문
dx=[0, 0, 1, -1]
dy=[1, -1, 0, 0]
answer=0
def dfs(x, y, path):
    global answer
    answer = max(answer, path)
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        # 범위 내 & 방문하지 않았다면
        if 0<=nx<r and 0<=ny<c and visited[ord(alpha[nx][ny])-65]==0:
            visited[ord(alpha[nx][ny])-65]=1
            dfs(nx, ny, path+1)
            visited[ord(alpha[nx][ny])-65]=0 # 백트레킹

dfs(0, 0, 1)
print(answer)