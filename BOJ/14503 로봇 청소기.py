# 2023.01.26
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # 세로, 가로
r, c, d = map(int, input().split()) # 좌표, 바라보는 방향 {0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽}
graph = [list(map(int, input().split())) for _ in range(n)]

direction = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 바라보는 방향 {0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽}
# 행, 열, 방향
def bfs(x, y, d):
    answer = 0 # 청소하면 +1
    queue = deque([[x, y]])
    graph[x][y]=2 # 청소
    answer+=1 # 현재 위치를 청소한다
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nextD = (d+3)%4 # 0->3->2->1 순서대로 시계반대방향으로 청소
            nx = a+direction[nextD][0]
            ny = b+direction[nextD][1]
            d =nextD
            # 2.1 왼쪽 방향에 아직 청소하지 않았다면
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0: 
                    queue.append((nx, ny))
                    graph[nx][ny]=2
                    answer+=1
                    break
            # 청소할 곳도 없고 다 벽이라면 후진
            elif i==3: 
                back = (d+2)%4
                nx = a+direction[back][0]
                ny = b+direction[back][1]
                queue.append([nx, ny])
                if graph[nx][ny]==1:
                    return answer

print(bfs(r, c, d))