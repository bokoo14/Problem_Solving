# 2023.01.14
import sys
input = sys.stdin.readline
import heapq

v, e = map(int, input().split()) # 정점, 간선
graph=[[] for _ in range(v+1)] 
for i in range(e): # 간선의 수만큼 반복
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])


heap=[[0, 1]] # weight, node 순으로 push
visited=[False]*(v+1)
answer=0
cnt=0
while heap:
    if cnt==v:
        break
    weight, node = heapq.heappop(heap) # 노드와 가중치
    if not visited[node]:
        answer+=weight
        visited[node]=True # 방문
        cnt+=1
        for i in graph[node]:
            heapq.heappush(heap, i)

print(answer)


