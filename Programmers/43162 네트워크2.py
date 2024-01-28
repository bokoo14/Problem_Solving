from collections import deque
        
def solution(n, computers):
    answer = 0  # 네트워크의 개수
    visited = [True] + [False] * (n) # n: 컴퓨터의 개수
    
    graph = [[] for _ in range(len(computers)+1)]
    graph[0] = [0]
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if computers[i][j] == 1: # 연결되어 있으면 그래프에 연결 표시
                graph[i+1].append(j+1)
                graph[j+1].append(i+1)
            
    for c in range(1, n+1): # 컴퓨터 모두 순회
        if visited[c] == False: # 방문하지 않았다면 
            answer += 1 # 네트워크 개수 하나 추가
            
            # DFS
            q = deque()
            q.append(c)
            
            while q:
                node = q.pop()
                visited[node] = True # 방문
                for n in graph[node]:
                    if visited[n] == False: # 방문하지 않았다면
                        q.append(n) # 방문하지 않았다면 다음에 방문할 노드에 추가하기
            
    return answer