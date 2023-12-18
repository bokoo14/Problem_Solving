#1389
#2022.07.25

'''
너비 우선 탐색
그래프 탐색
너비 우선 탐색
플로이드-워셜
'''
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

friend=[[] for _ in range(N+1)]
for i in range(0, M):
    A, B=map(int, sys.stdin.readline().split())
    friend[A].append(B)
    friend[B].append(A)

def bfs(x):
    num=[0]*(N+1)
    queue=deque()
    visited[x]=True
    queue.append(x)
    while queue:
        v=queue.popleft()
        for i in friend[v]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                num[i]=num[v]+1
    return sum(num)

answer=[]
for i in range(1, N+1):
    visited=[False]*(N+1)
    answer.append(bfs(i))
print(answer.index(min(answer))+1)
