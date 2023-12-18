# 2022.12.30
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = list(map(int, input().split()))
number = sorted(number)

answer = []
def backtracking():
    if len(answer)==m:
        print(' '.join(map(str, answer)))
        return

    for i in number:
        if i not in answer:
            answer.append(i)
            backtracking()
            answer.pop()

backtracking()


