#1707
#2022.08.01

import sys
from collections import deque

def bfs(start, check):
    queue=deque([x])
    



    while queue:
        a=queue.popleft()
        



k=int(sys.stdin.readline())

for i in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph=[[] for _ in range(v+1)]
    visited=[False]*(v+1)
    for j in range(e):
        a, b= map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

            
