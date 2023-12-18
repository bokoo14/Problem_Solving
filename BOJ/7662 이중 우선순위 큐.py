import sys
input = sys.stdin.readline
import heapq
# 우선순위 큐 힙 라이브러리 사용 -> min heap만 지원

t = int(input())
for i in range(t):
    k=int(input())
    visited=[0]*(k)
    minHeap=[]
    maxHeap=[]
    for j in range(k):
        a, b = map(str, input().split())
        if a=="I": # 삽입
            heapq.heappush(minHeap, [int(b), j])
            heapq.heappush(maxHeap, [-int(b), j])
            visited[j]=1
        elif a=="D": # 삭제
            if b=="-1": # 최소값 삭제
                while minHeap and visited[minHeap[0][1]]==0: # 힙에는 존재하지만 이미 삭제된 노드라면
                    heapq.heappop(minHeap)
                if minHeap: # 동기화 후 제일 작은 값을 삭제시켜줌
                    visited[minHeap[0][1]]=0
                    heapq.heappop(minHeap)
            elif b=="1": # 최대값 삭제
                while maxHeap and visited[maxHeap[0][1]]==0:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]]=0
                    heapq.heappop(maxHeap)

    while minHeap and visited[minHeap[0][1]]==0:
        heapq.heappop(minHeap)
    while maxHeap and visited[maxHeap[0][1]]==0:
        heapq.heappop(maxHeap)

    if maxHeap and minHeap:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print("EMPTY")
