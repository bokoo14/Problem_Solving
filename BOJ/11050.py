#11050
#2022.06.30

import sys
import math

N, K=map(int, sys.stdin.readline().split())

answer=math.factorial(N)/(math.factorial(N-K))/math.factorial(K)
print(int(answer))
