# 2023.02.04
import sys
input = sys.stdin.readline
from collections import defaultdict

s = input().rstrip()
alpha = list(map(int, str(input().rstrip()))) # 좋은 알파벳: 1, 나쁜 알파벳: 0
k=int(input()) # 나쁜 알파벳의 최대 개수

dic = defaultdict(list)
for i in range(len(s)):
    index = ord(s[i])-97
    if alpha[index]==0: # 나쁜 알파벳이라면
        dic[alpha[index]].append(i)
    
print(dic)
