#11650
#2022.06.28

import sys

N = int(sys.stdin.readline())

points = []
for i in range(0, N):
    points.append(list(sys.stdin.readline().split()))

#x좌표가 증가하는 순서대로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
points.sort(key=lambda x:int(x[1]))
points.sort(key=lambda x:int(x[0]))

for i in range(0, N):
    print(points[i][0], points[i][1])

