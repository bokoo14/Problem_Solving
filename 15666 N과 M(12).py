import sys
input = sys.stdin.readline

n, m = map(int, input().split())
number = sorted(list(map(int, input().split())))

answer = []
def backtracking(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return 

    tmp = 0
    for i in range(start, n):
        if tmp !=number[i]:
            tmp = number[i]
            answer.append(number[i])
            backtracking(i)
            answer.pop()


backtracking(0)
