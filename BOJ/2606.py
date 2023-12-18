#2606
#2022.07.08

import sys

n=int(sys.stdin.readline()) #컴퓨터의 수
m=int(sys.stdin.readline()) #네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

computer=[[]*n for i in range(n+1)]
    
for j in range(m):
    a,b=map(int, sys.stdin.readline().split())
    computer[a].append(b)
    computer[b].append(a)

visited=[0]*(n+1)
count=0
def dfs(start):
    global count
    visited[start]=1
    for i in computer[start]:
        if visited[i]==0:
            dfs(i)
            count+=1
            

dfs(1)
print(count)
