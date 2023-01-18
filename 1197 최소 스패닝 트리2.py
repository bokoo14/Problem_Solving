# 2023.01.18
import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split())
graph=[[] for _ in range(v+1)] # 노드의 수
for i in range(e):
    a, b, c = map(int, input().split()) # 노드1, 노드2, 가중치
    graph[a].append([c, b]) 
    graph[b].append([c, a])

heap=[[0, 1]]
visited=[0]*(v+1)
answer=0
while heap:
    if sum(visited)==v: # 모든 노드를 연결하였다면? 
        break
    weight, node = heapq.heappop(heap)
    if not visited[node]: # 방문하지 않은 노드라면? 해당 노드를 연결
        answer+=weight
        visited[node]=1
        for i in graph[node]: # 현재 노드와 연결되어 있는 모든 노드를 minHeap에 넣어줌
            heapq.heappush(heap, i)

print(answer)