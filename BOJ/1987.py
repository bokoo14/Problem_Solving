#1987
#2022.07.29

import sys
from collections import deque

R, C= map(int, sys.stdin.readline().split()) #행, 열
alpha=[list(sys.stdin.readline().strip()) for _ in range(R)]

visited=[False]*(26) #dp table
first=ord(alpha[0][0])-65 #아스키코드 활용
visited[first]=True

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
maxnum=0
def dfs(x, y, cnt):
    global maxnum

    maxnum=max(cnt, maxnum) #방문 횟수의 최대 구하기
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<R and 0<=ny<C and visited[ord(alpha[nx][ny])-65]==False:
            asc=ord(alpha[nx][ny])-65
            visited[asc]=True
            ncnt=cnt+1
            dfs(nx, ny, ncnt)
            visited[asc]=False #백트레킹
            
dfs(0, 0, 1)
print(maxnum)
