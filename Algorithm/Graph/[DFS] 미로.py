import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# n*m크기의 2차원 미로
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

# 4방향으로 이동 가능 -> 왼쪽, 오른쪽 위쪽, 아래쪽으로 한 칸 씩만 이동 가능
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited=[[0]*m for _ in range(n)]
answer=10**9
def dfs(x, y, depth, visited):
    global answer
    if x==n-1 and y==m-1: # 탈출->최소 이동횟수
        answer = min(answer, depth)
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m: #미로의 범위 안 이면
                if maze[nx][ny]==1 and visited[nx][ny]==0:
                    visited[x][y]=1 # 방문(두번 방문하지 못하게)
                    dfs(nx, ny, depth+1, visited)
                    visited[x][y]=0 # 초기화
    return answer
    

print(dfs(0, 0, 0, visited))

