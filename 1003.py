#1003
#2022.06.30

'''
피보나치 수열의 규칙을 찾는 문제
zero는 1, 0, 1로 나열
one은 0, 1, 1로 나열
그 후 n 번째부터는 피보나치 수열 "N2=N1+N0"로 나열됨
'''

import sys

N=int(sys.stdin.readline())

zero=[1, 0, 1]
one=[0, 1, 1]

def fibo(n):
    if len(zero)<=n:
        for i in range(len(zero), n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])

    print(zero[n], one[n])

for i in range(0, N):
    value=int(sys.stdin.readline())
    fibo(value)
    
