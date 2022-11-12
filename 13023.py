#13023
#2022.08.03
#깊이 우선 탐색
import sys
input=sys.stdin.readline

N, M = map(int, input().split()) #사람 수, 친구 관계의 수
graph=[[]*(1) for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited=[False]*(N)
#깊이 우선 탐색
def dfs(x, depth):
    if depth==5:
        print("1")
        exit(0)
    for i in graph[x]:
        if not visited[i]:
            visited[i]=True
            dfs(i, depth+1)
            visited[i]=False

for i in range(N):
    visited[i]=True
    dfs(i, 1)
    visited[i]=False
print(0)


