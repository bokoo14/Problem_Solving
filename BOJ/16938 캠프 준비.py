# 2023.01.18
# 조합
import sys
input = sys.stdin.readline
from itertools import combinations

n, l, r, x = map(int, input().split())
problem = list(map(int, input().split()))

answer=0
for i in range(2, n+1): # 2~n개의 수를 선택 가능
    for subProb in combinations(problem, i):
        if l<=sum(subProb)<=r and abs(max(subProb)-min(subProb))>=x:
            answer+=1

print(answer)

'''
# 비트마스킹, 백트래킹
# https://recordofwonseok.tistory.com/383

'''