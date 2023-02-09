# 2023.02.09
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())
robot = [[] for _ in range(n)]
for i in range(n):
    a, b, c = map(str, input().split())
    robot[i].append([int(a), int(b), c])

order = [[] for _ in range(m)]
for i in range(m):
    a, b, c = map(str, input().split())
    order[i].append([int(a), b, c])

