#1012
#2022.07.09
'''
dfs방식으로 풀이
'''
import sys

T=int(sys.stdin.readline())

dx=[1, -1, 0, 0]
dy=[0, 0, -1, 1]
def bfs(x,y):
    queue=[[x,y]]
    while queue:
        a, b=queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q=a+dx[i]
            w=b+dy[i]
            if 0<=q<N and 0<=w<M and field[q][w]==1:
                field[q][w]=0
                queue.append([q, w])


for i in range(0, T):
    M, N, K= map(int, sys.stdin.readline().split())
    field=[[0]*M for i in range(N)]
    cnt=0
    for j in range(0, K):
        a, b=map(int, sys.stdin.readline().split())
        field[b][a]=1
        
    for k in range(0, N):
        for p in range(0, M):
            if field[k][p]==1:
                bfs(k, p)
                field[k][p]=0
                cnt+=1
    print(cnt)
