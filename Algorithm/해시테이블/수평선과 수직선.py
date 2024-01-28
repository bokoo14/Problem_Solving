'''
N개의 좌표가 주어졌을 때, 이 좌표들을 연결하는 선들 중에서 수직선과 수평선의 개수를 출력하시오.
예를 들어, 4개의 좌표 (0, 0) (1, 0) (0 1) (1 1) 이 주어지면 2개의 수직선과 2개의 수평선이 생긴다.
'''

import sys
input = sys.stdin.readline

n = int(input())
number = [list(map(int, input().split())) for _ in range(n)]


xpoint = {} # 수직선
ypoint = {} # 수평선
def sol(number):
    for x, y in number:
        if x in xpoint:
            xpoint[x]+=1
        else:
            xpoint[x]=1

        if y in ypoint:
            ypoint[y]+=1
        else:
            ypoint[y]=1

sol(number)
xanswer = [x for x in xpoint.values() if x>1]
yanswer = [y for y in ypoint.values() if y>1]
print(len(xanswer))
print(len(yanswer))

