# 2023.01.17
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # 사다리, 뱀
graph=[i for i in range(101)] # 0~100까지 게임판
for i in range(n+m):
    a, b = map(int, input().split()) # a->b이동
    graph[a]=b

visited=[0]*(101) # 방문 여부 & 주사위를 던진 횟수
def bfs(start):
    queue=deque([start]) # 시작점: 1
    #visited[start]=1
    while queue:
        current=queue.popleft()
        for i in range(1, 7): # 주사위 던지기
            total=current+i # (사다리로 이동한 값 or 뱀으로 이동한 값 or 현재 위치)+(주사위 값)
            if total>100:
                continue
            next=graph[total]  # (사다리로 이동한 값 or 뱀으로 이동한 값 or 현재 위치)+(주사위 값)
            if not visited[next]:
                queue.append(next)
                visited[next]=visited[current]+1
                if next==100:
                    return
bfs(1)
print(visited[100])