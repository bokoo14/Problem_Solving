#11286
#2022.08.02
import sys
import heapq

'''
절댓값이 가장 작은 값이 우선순위가 높아질 수 있도록
(abs(x), x): 튜플 형식으로 힙에 추가한다
튜플로 구성-> 맨 앞 숫자만을 가지고 정렬
'''

N= int(sys.stdin.readline())

heap=[]
for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    elif x==0:
        if len(heap)!=0:
            print(heapq.heappop(heap)[1])
        elif len(heap)==0:
            print(0)
            
