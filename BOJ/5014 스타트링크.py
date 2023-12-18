# 2023.01.24
import sys
input = sys.stdin.readline
from collections import deque

# 총 f층, 지금 s층, 원하는 g층, 위로 u층 이동, 아래로 d층 이동
f, s, g, u, d = map(int, input().split())

visited=[False]*(f+1) # 방문여부
stair=[0]*(f+1)
queue=deque()
# 너비 우선 탐색
def bfs(current): # 현재 층수
    queue.append(current)
    visited[current]=True
    while queue:
        c = queue.popleft() # 현재 몇층인지?
        if c == g: # 원하는 층에 도달하였으면
            return stair[g]
        for next in (c+u, c-d): # 위로 올라가는 경우 & 밑으로 내려가는 경우
            if 0<next<=f and not visited[next]:
                stair[next]=stair[c]+1
                visited[next]=True
                queue.append(next)
    return "use the stairs"

print(bfs(s))