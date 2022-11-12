#2630
#2022.07.25

import sys

N=int(sys.stdin.readline())

paper=[list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white=0
blue=0
def cutting(x, y, n):
    global white, blue

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y]!=paper[i][j]:
                cutting(x, y, n//2)
                cutting(x+n//2, y, n//2)
                cutting(x, y+n//2, n//2)
                cutting(x+n//2, y+n//2, n//2)
                return
                
    if paper[x][y]==0:
        white+=1
    elif paper[x][y]==1:
        blue+=1


cutting(0, 0, N)
print(white)
print(blue)
