# 2023.05.30
from collections import deque


def solution(n, computers):
    answer = 0  # 네트워크의 개수
    visited = [0] * n  # 컴퓨터의 개수: n

    def BFS(start):
        q = deque([start])
        while q:
            tmp = q.popleft()
            visited[tmp] = 1  # 꺼낸 후 방문하기
            for i in range(len(computers[tmp])):
                # 현재 해당하는 노드에 연결된 모든 노드를 큐에 넣어줌 - 방문하지 않았고, 연결되어 있다면
                if visited[i] == 0 and computers[tmp][i] == 1:
                    q.append(i)  # 연결된 노드를 큐에 추가

    # visited에서 방문하지 않은 노드를 방문 -> BFS를 통해 연결된 노드는 모두 방문 -> 연결되지 않은 노드만 0으로 남아있음
    while 0 in visited:
        answer += 1
        BFS(visited.index(0))

    return answer


# print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
