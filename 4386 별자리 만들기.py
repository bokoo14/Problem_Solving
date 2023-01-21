# 2023.01.20
import sys
input = sys.stdin.readline
import heapq

n = int(input()) # 별의 개수
stars = [list(map(float, input().split())) for _ in range(n)]

# 모든 별들 사이의 거리
graph = [[] for _ in range(n)]
for i in range(n):
    x1, y1 = stars[i] 
    for j in range(n):
        if i==j:
            continue
        x2, y2 = stars[j]
        length = ((x2-x1)**2+(y2-y1)**2)**0.5
        graph[i].append([j, length]) # 연결된 별, 길이

visited=[False]*(n) # n개의 별
heap=[[0, 0]] #길이, 별
starNum=n # 별의 수
answer=0
while starNum:
    length, node = heapq.heappop(heap)
    if visited[node]:
        continue
    starNum-=1
    visited[node]=True
    answer+=length
    for thisStar, thisLength in graph[node]:
        if visited[thisStar]:
            continue
        heapq.heappush(heap, [thisLength, thisStar])

print(answer)