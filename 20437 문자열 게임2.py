# 2023.02.03
import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
for _ in range(t):
    w = input().rstrip()
    k = int(input())
    dic = defaultdict(list) 
    for i in range(len(w)): # 문자열의 index
        if w.count(w[i])>=k: # 해당하는 index의 문자열의 개수가 k보다 크다면
            dic[w[i]].append(i)

    if not dic: # 딕셔너리에 아무 값도 없으면 답이 없음
        print(-1)
    else:
        answer1=10**9
        answer2=0
        for i in dic: # 알파벳과 index를 저장한 dic
            for j in range(0, len(dic[i])-k+1): # 원하는 문자가 k개 이상 포함되어야 함->마지막 index: len(dic[i])-k
                answer1=min(answer1, dic[i][j+k-1]-dic[i][j]+1)
                answer2=max(answer2, dic[i][j+k-1]-dic[i][j]+1)
        print(answer1, answer2)