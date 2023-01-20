# 2023.01.20
import sys
input = sys.stdin.readline
import heapq

n = int(input()) # 별의 개수
stars = [list(map(float, input().split())) for _ in range(n)]

graph = [[] for _ in range(n)]
for i in range(n):
    x1, y1 = stars[i]
    for j in range(n):
        if i==j:
            continue
        x2, y2 = stars[j]
        length = ((x2-x1)**2+(y2-y1)**2)**0.5
        graph[i].append([j, length])

visited=[False]*(n)
heap=[[0, 0]]
nodeNum=n
answer=0
while nodeNum:
    length, node = heapq.heappop(heap)
    if visited[node]:
        continue
    nodeNum-=1
    visited[node]=True
    answer+=length
    for x, y in graph[node]:
        if visited[x]:
            continue
        heapq.heappush(heap, [x, y])

print(answer)