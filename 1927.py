#1927
#2022.07.23

import sys
import heapq

N=int(sys.stdin.readline())

heap=[]
for i in range(0, N):
    k=int(sys.stdin.readline())
    
    if k==0:
        if len(heap)==0:
            print("0")
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, k)
    
