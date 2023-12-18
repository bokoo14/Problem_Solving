# 2023.02.01
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q=deque([x])
    while q:
        x, y = q.popleft()
        if 

while True:
    n, m = map(int, input().split())
    if n==0 and m==0:
        break
    graph = [[] for _ in range(m)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited=[[False]*(n-1) for _ in range(n)] # 정점 방문 check

