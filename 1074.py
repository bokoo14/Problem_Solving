#1074
#2022.07.25
'''
분할정복
재귀
'''
import sys

#2**N, 행, 열
N, r, c = map(int, sys.stdin.readline().split())

answer=0
def reach(a, x, y):
    global answer

    if x==r and y==c:
        print(answer)
        exit(0)

    if a==1:
        answer+=1
        return
    if not (x<=r<x+a and y<=c<y+a):
        answer+=a*a
        return

    reach(a//2, x, y)
    reach(a//2, x, y+a//2)
    reach(a//2, x+a//2, y)
    reach(a//2, x+a//2, y+a//2)


reach(2**N, 0, 0)

