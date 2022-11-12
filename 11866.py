#11866
#2022.06.28

import sys

N, K = map(int, sys.stdin.readline().split())

circle=[]
for i in range(0, N):
    circle.append(i+1)

removed=[]
index=0
for i in range(0, N):
    index=(index+K-1)%len(circle)
    get=circle[index]
    removed.append(get)
    del circle[index]


print("<", end="")
for i in range(0, N-1):
      print(removed[i], end=", ")
print(removed[N-1], end="")
print(">", end="")
