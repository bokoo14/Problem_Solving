import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

def sol(n, k):
    if n==1:
        return 1
    else:
        return (sol(n-1, k)+k)%n +1

print(sol(n, 1)-1)