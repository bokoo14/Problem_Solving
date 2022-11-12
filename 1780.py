#1780
#2022.07.25

'''
분할정복, 재귀
'''
import sys

N=int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

neg=0
zero=0
pos=0

def cutting(x, y, n):
    global neg, zero, pos

    check=paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j]!=check:
                for k in range(0, 3):
                    for l in range(0, 3):
                        cutting(x+k*n//3, y+l*n//3, n//3)
                return

    if check==-1:
        neg+=1
    elif check==0:
        zero+=1
    elif check==1:
        pos+=1

cutting(0, 0, N)
print(neg)
print(zero)
print(pos)
