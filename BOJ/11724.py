#11724
#2022.07.23

'''
파이썬은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임 에러
->sys.setrecursionlimit(10000)으로 재귀 제한 설정!!
'''
import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())

graph=[[] for _ in range(N+1)]
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(x):
    visited[x]=True
    for i in graph[x]:
        if visited[i]==False:
            dfs(i)
            

visited=[False]*(N+1)
cnt=0
for i in range(1, N+1):
    if visited[i]==False:
        cnt+=1
        dfs(i)


print(cnt)
