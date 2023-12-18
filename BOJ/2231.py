#2231
#2022.07.01

'''
브루트포스 알고리즘
:가능한 모든 경우의 수를 탐색하면서 정답이 되는 결과를 모두 가져온다
시간이 오래 걸린다
완전 탐색 알고리즘
'''

import sys

N=int(sys.stdin.readline())

#가능한 모든 수 탐색
result=0
for i in range(0, N+1):
    num=str(i)
    num=list(map(int, num))
    
    result = sum(num)+i

    if N==result:
        print(i)
        break

    if i==N:
        print(0)
