# 2023.06.27
import sys
input = sys.stdin.readline

m = int(input())
score = list(map(int, input().split()))

answer = sum(score)/max(score)*100/len(score)
print(answer)