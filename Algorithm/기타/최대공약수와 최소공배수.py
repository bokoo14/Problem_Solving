import sys
input=sys.stdin.readline

N, M = map(int, input().split())

# 최대공약수
def gcd(n,m):
    if m==0:
        return n
    elif m>0:
        return gcd(m, n%m)

#최소공배수
def lcm(n,m):
    return n*m//gcd(N,M)

print(gcd(N,M))
print(lcm(N,M))