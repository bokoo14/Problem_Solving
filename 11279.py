#11279
#2022.07.10

'''
heapq는 min heap만을 지원
num을 음수로 만들어서 저장
출력할때는 다시 -1을 곱해서 출력

음수로 저장해서 max heap을 구현한다
'''

import sys
import heapq

n=int(sys.stdin.readline())

array=[]
for i in range(n):
    k=int(sys.stdin.readline())
    
    if k==0:
        if len(array)==0:
            print("0")
        else:
            print(-1*heapq.heappop(array)) #min heap만을 지원->-1로 만들어줌
    else:
        heapq.heappush(array, (-k))


'''
리스트 시간 초과
import sys

n=int(sys.stdin.readline())

array=[]
for i in range(n):
    k=int(sys.stdin.readline())
    m=0
    if k==0:
        if len(array)==0:
            print("0")
        else:
            m=max(array)
            print(m)
            array.remove(m)
    else:
        array.append(k)

'''
