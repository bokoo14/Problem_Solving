#1676
#2022.06.30

import sys
import math

N=int(sys.stdin.readline())

facto=(math.factorial(N))
facto=str(facto)
facto=list(facto)
facto.reverse()

answer=0

for i in range(0, N):
    if facto[i]!='0':
        answer=i
        break

print(answer)

