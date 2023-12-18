#1929
#2022.07.09

import sys
import math
M, N=map(int, sys.stdin.readline().split())

def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num%i==0:
                return False
        return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)
