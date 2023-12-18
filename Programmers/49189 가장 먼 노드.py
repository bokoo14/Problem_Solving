# 2023.06.06
# 프로그래머스 49189 가장 먼 노드
from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)  # 방문여부
    distance = [0] * (n + 1)  # 1에서의 거리를 저장하는 배열

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    queue = deque([1])  # 첫 노드를 방문 - 1노드부터 시작
    visited[1] = True

    # BFS
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:  # 방문하지 않았다면 방문해줌 -> 큐에 저장
                queue.append(i)
                visited[i] = True
                distance[i] = distance[v] + 1  # 거리를 +1씩 늘려줌

    max_distance = max(distance)  # 리스트에서 가장 긴 거리를 측정함
    for d in distance:
        if d == max_distance:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
