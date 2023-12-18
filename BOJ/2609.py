#2609
#2022.07.01

import sys

N, K= map(int, sys.stdin.readline().split())

#최대공약수 GCD알고리즘 유클리드호제법
def gcd(a, b):
    while b>0:
        a,b=b,a%b
    return a

#최소공배수
def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(N, K))
print(lcm(N, K))


'''
#내장 함수 활용
import math
import sys

a, b=map(int, sys.stdin.readline().split())

print(math.gcd(a, b))
print(math.lcm(a, b))
'''
