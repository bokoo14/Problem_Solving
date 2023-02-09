# 2023.02.09
import sys
input = sys.stdin.readline
import heapq

n = int(input())

h = []
for i in range(n):
    num = list(map(int, input().split()))
    for j in range(n):
        if len(h)<n:
            heapq.heappush(h, num[j])
        else:
            if h[0]<num[j]:
                heapq.heappop(h)
                heapq.heappush(h, num[j])

print(h[0])