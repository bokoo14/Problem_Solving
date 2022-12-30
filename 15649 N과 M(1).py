# 2022.12.30
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

answer = []
def backtracking():
    if len(answer)==m:
        print(' '.join(map(str, answer)))
    
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            backtracking()
            answer.pop()

backtracking()