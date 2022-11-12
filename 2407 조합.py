#2047 조합
#2022.08.21
import sys
input=sys.stdin.readline

def fac(k):
    if k==0:
        return 1
    return fac(k-1)*(k)


n, m = map(int, input().split())
answer = fac(n)//fac(n-m)//fac(m)
print(int(answer))
