#11399 ATM
#2022.06.30

import sys

N=int(sys.stdin.readline())

money=[]
money=list(map(int, sys.stdin.readline().split()))

money.sort()

m_sum=0
for i in range(0, N):
    m_sum+=sum(money[0:i+1])

print(m_sum)
