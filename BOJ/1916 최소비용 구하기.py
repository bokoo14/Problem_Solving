# 2023.01.12
import sys
input=sys.stdin.readline
import heapq

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split()) 
    graph[a].append((b, c))
start, end = map(int, input().split())

def dijkstra(start):
    distance=[10**9]*(n+1) # 비용 저장
    heap=[] 
    heapq.heappush(heap, (start, 0)) #최소힙
    distance[start]=0 # 시작점의 비용은 0
    while heap:
        current, weight = heapq.heappop(heap)
        if distance[current]<weight: # 최단거리를 갱신한 노드는 다시 확인하지 않음
            continue
        for c, w in graph[current]: # 다음으로 이동할 노드를 갱신시켜줌
            if distance[c] > weight+w: # c까지 가는 경로가 더 최소 비용이라면
                distance[c]=weight+w
                heapq.heappush(heap, (c, weight+w))

    return distance[end]

print(dijkstra(start))