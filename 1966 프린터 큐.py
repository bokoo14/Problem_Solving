import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    paper = list(map(int, input().split()))
    print(paper)
