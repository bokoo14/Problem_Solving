# 2023.01.23
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split()) # start, end
m = int(input())

graph = [[] for _ in range(n+1)] # n명의 사람들
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited=[False]*(n+1)
def dfs(current,depth):
    visited[current]=True # 방문 check
    if current == b: # 목표에 도달하였으면 깊이를 return
        print(depth)
        exit(0)

    # 모든 연결된 노드 & 방문하지 않은 노드를 check해줌
    for i in graph[current]:
        if not visited[i]:
            dfs(i, depth+1)
    
dfs(a, 0)
print(-1)