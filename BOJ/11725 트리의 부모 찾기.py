import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

answer=[-1]*(n+1)
def dfs(vertex):
    for i in tree[vertex]:
        if answer[i]==-1:
            answer[i]= vertex
            dfs(i)

dfs(1)
for i in range(2, n+1):
    print(answer[i])