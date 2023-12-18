#11651
#2022.06.28

import sys

N = int(sys.stdin.readline())

points=[]
for i in range(0, N):
    points.append(list(sys.stdin.readline().split()))

points.sort(key=lambda x:int(x[0]))
points.sort(key=lambda x:int(x[1]))

for i in range(0, N):
    print(points[i][0], points[i][1])
