# 2023.02.09
import sys
input = sys.stdin.readline

a, b = map(int, input().split()) # 가로, 세로
n, m = map(int, input().split())
board = [[0]*(a) for _ in range(b)]
NESW = {"N":0, "E":1, "S":2, "W":3}
direction = [[0, -1],[1, 0],[0, 1],[-1, 0]] # N, E, S, W

# 로봇의 초기 위치
robot = [[] for _ in range(n)]
for i in range(n):
    ra, rb, rc = input().split() # x, y, 방향
    robot[i].append([ra, rb, NESW[rc]])
    x = int(a)-1
    y = b- int(rb)
    board[x][y] = i+1

# 명령
order = [[] for _ in range(m)]
for i in range(m):
    ca, cb, cc = input().split() # 명령을 내리는 로봇, 종류, 반복회수
    order[i].append([ca, NESW[cb], cc])


