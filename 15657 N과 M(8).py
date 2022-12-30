# 2022.12.30
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
number = sorted(number)

answer = []
def backtracking(start):
    if len(answer)==m:
        print(' '.join(map(str, answer)))
        return 

    for i in range(start, n):
        answer.append(number[i])
        backtracking(i)
        answer.pop()

backtracking(0)