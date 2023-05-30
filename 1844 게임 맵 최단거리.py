# 2023.05.30

from collections import deque


def solution(maps):
    answer = 0
    n = len(maps[0])
    m = len(maps)
    visited = [[0] * n for _ in range(m)]  # 방문 여부 check
    visited[0][0] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(x, y):
        # q = deque([[x, y]])
        q = deque()
        q.append([x, y])
        while q:
            xx, yy = q.popleft()
            if xx == m - 1 and yy == n - 1:  # 도착했다면
                break
            for i in range(4):
                nx = xx + dx[i]
                ny = yy + dy[i]
                if 0 <= nx < m and 0 <= ny < n:  # 사각형을 넘지 않았을때 - m과 n을 잘보자
                    # 다음으로 갈 방향이 길&방문하지 않았다면
                    if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                        q.append([nx, ny])
                        visited[nx][ny] = visited[xx][yy] + 1

        # visited[m-1][n-1]이 0이라면, 도착할 수 없는 곳이라는 뜻
        if visited[m - 1][n - 1] == 0:
            return -1
        else:
            return visited[m - 1][n - 1]

    answer = bfs(0, 0)
    return answer


# 0: 벽, 1: 길
print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 0, 0, 0, 1],
        ]
    )
)


# print(
#     solution(
#         [
#             [1, 0, 1, 1, 1],
#             [1, 0, 1, 0, 1],
#             [1, 0, 1, 1, 1],
#             [1, 1, 1, 0, 0],
#             [0, 0, 0, 0, 1],
#         ]
#     )
# )
