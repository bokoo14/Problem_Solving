#1260
#2022.07.20

import sys
from collections import deque

#깊이 우선 탐색
def dfs(x):
    visited[x]=True
    print(x, end=' ')
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

        
#너비 우선 탐색
def bfs(x):
    queue=deque([x])
    visited[x]=True
    while queue:
        v=queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

#정점, 간선, 탐색을 시작할 정점의 번호
N, M, V = map(int, sys.stdin.readline().split())

graph=[[] for i in range(N+1)]
for i in range(0, M):
    a, b=map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()


visited=[False]*(N+1)
dfs(V)
print()

visited=[False]*(N+1)
bfs(V)
