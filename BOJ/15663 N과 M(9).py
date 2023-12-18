# 2022.12.30
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = sorted(list(map(int, input().split())))

answer = []
visited = [0]*(n)
def backtracking():
    if len(answer)==m:
        print(' '.join(map(str, answer)))
        return

    tmp=0
    for i in range(0, n):
        if visited[i]==0 and tmp !=number[i]:
            answer.append(number[i])
            visited[i]=1
            tmp=number[i]
            backtracking()
            answer.pop()
            visited[i]=0

backtracking()
