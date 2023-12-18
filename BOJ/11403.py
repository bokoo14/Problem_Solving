#11403
#2022.08.02

'''
프로이드 워셜 알고리즘
for문을 3번 써서 정점을 연결할 수 있는지 판단
첫 번째 for문은 중간 경로

print(*arr)를 사용하면 대괄호 없이 한번에 출력할 수 있음
리스트에 Asterisk(*)를 사용하면 리스트 압축 해제를 할 수 있음
'''

import sys
INF=sys.maxsize

N = int(sys.stdin.readline()) #정점의 개수
graph=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

distance=[[INF]*N for _ in range(N)]
for k in range(N): #중간경로
    for i in range(N): #행
        for j in range(N): #열
            if graph[i][j]==1 or (graph[i][k]==1 and graph[k][j]==1):
                graph[i][j]=1
                
for i in range(N):
    print(*graph[i])
