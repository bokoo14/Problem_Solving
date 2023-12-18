#1992
#2022.07.26

'''
분할정복, 재귀
'''
import sys

N=int(sys.stdin.readline())

#video=[list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

video=[]
for i in range(0, N):
    video.append(list(map(int, sys.stdin.readline().strip())))


def quad(x, y, n):
    compare=video[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if compare!=video[i][j]:
                print("(", end="")
                quad(x, y, n//2)
                quad(x, y+n//2, n//2)
                quad(x+n//2, y, n//2)
                quad(x+n//2, y+n//2, n//2)
                print(")", end="")
                return

    print(compare, end="")


quad(0, 0, N)
                
