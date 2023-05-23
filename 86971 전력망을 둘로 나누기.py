# 프로그래머스 86971 전력망을 둘로 나누기 - 완전 탐색


# 전력망을 둘로 나누었을 때, 두 전력망의 송전탑 개수의 차이를 최소화
# 전력망을 둘로 나누는 방법은 전력망을 구성하는 모든 선분 중 하나를 제거하는 것
def solution(n, wires):
    answer = 10**9

    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # 모든 선분을 하나씩 제거해보면서 송전탑 개수의 차이를 구함
    for i in range(len(wires)):
        # i번째 선분 제거
        graph[wires[i][0]].remove(wires[i][1])
        graph[wires[i][1]].remove(wires[i][0])

        # BFS
        visited = [False] * (n + 1)
        queue = [1]
        visited[1] = True
        cnt = 0  # 송전탑의 개수

        while queue:
            v = queue.pop(0)
            cnt += 1
            for j in graph[v]:
                if not visited[j]:  # 방문하지 않았다면
                    queue.append(j)
                    visited[j] = True

        answer = min(abs((n - cnt) - cnt), answer)

        # i번째 선분 복구
        graph[wires[i][0]].append(wires[i][1])
        graph[wires[i][1]].append(wires[i][0])

        return answer  # 송전탑 개수의 차이


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
