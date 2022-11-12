#1697
#2022.07.25
'''
그래프 이론, 그래프 탐색, 너비 우선 탐색
queue는 매우 느리고 시간초과의 원인
->from collections import deque를 써서 덱을 써야 한다

queue: 한쪽으로만 입력 가능, 반대쪽으로만 출력 가능
deque: 양쪽으로 입출력 가능
'''
import sys
from collections import deque
#현재 위치, 목표 위치
N, K = map(int, sys.stdin.readline().split())

dist=[0]*(100001)
#너비 우선 탐색
def bfs(x):
    queue=deque()
    queue.append(x)
    while queue:
        v=queue.popleft()
        if v==K:
            print(dist[v])
            break
        for i in (v-1, v+1, v*2):
            if 0<=i<=100000 and dist[i]!=0:
                dist[i]=dist[v]+1
                queue.append(i)

bfs(N)


