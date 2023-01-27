# 2023.01.27
import sys
input = sys.stdin.readline
from collections import deque

def bfs(startX, startY, store, endX, endY):
    visited=[False]*(len(store)) # 편의점 방문 check
    q = deque([[startX, startY]])
    while q:
        a, b = q.popleft()
        if (abs(a-endX)+abs(b-endY))<=1000: # 현재 위치에서 페스티벌에 갈 수 있는지 check
            return "happy"
        for i in range(len(store)): # 현재 위치에서 편의점에 갈 수 있는지 check & 방문하지 않은 편의점만
            if not visited[i]:
                n, m = store[i]
                if (abs(a-n)+abs(b-m))<=1000:
                    q.append([n, m])
                    visited[i]=True
    return "sad" # 현재 위치에서 페스트벌도 못가고 편의점도 가지 못한다면

t = int(input())
for i in range(t):
    n = int(input()) # 맥주를 파는 편의점의 개수
    startX, startY = map(int, input().split()) # 상근이네 집
    store = [list(map(int, input().split())) for _ in range(n)] # 편의점
    endX, endY = map(int, input().split()) # 락 페스티벌

    print(bfs(startX, startY, store, endX, endY))