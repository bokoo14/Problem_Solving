#7562
#2022.08.04
#너비우선탐색

import sys
input=sys.stdin.readline
from collections import deque

#시계방향으로 이동할 수 있는 경우의 수들
dx=[-2, -1, 1, 2, 2, 1, -1, -2] #행
dy=[1, 2, 2, 1, -1, -2, -2, -1] #열

def bfs(x, y):
    queue=deque()
    queue.append([x, y])
    
    while queue:
        a, b= queue.popleft()
        if a==x2 and b==y2:
            print(chess[x2][y2])
            return 
        for i in range(8):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<length and 0<=ny<length and chess[nx][ny]==0:
                chess[nx][ny]=chess[a][b]+1
                queue.append([nx, ny])
            
n=int(input()) #테스트 케이스         
for i in range(n):
    length=int(input()) #체스판의 한 변의 길이
    x1, y1 = map(int, input().split()) #현재 있는 칸
    x2, y2 = map(int, input().split()) #이동하려고 하는 칸
    chess=[[0]*length for _ in range(length)]
    bfs(x1, y1)
    
