#1764
#2022.06.30

'''
list를 set으로 바꾸면 합집합, 교집합, 차집합, 대칭차집합을 쉽게 구할 수 있음
https://zetawiki.com/wiki/Python_%EB%A6%AC%EC%8A%A4%ED%8A%B8_%ED%95%A9%EC%A7%91%ED%95%A9,_%EA%B5%90%EC%A7%91%ED%95%A9,_%EC%B0%A8%EC%A7%91%ED%95%A9,_%EB%8C%80%EC%B9%AD%EC%B0%A8

strip()으로 앞뒤 공백 문자 제거
'''

import sys

N, M = map(int, sys.stdin.readline().split())

D=[]
for i in range(0, N):
    D.append(sys.stdin.readline().strip())

B=[]
for i in range(0, M):
    B.append(sys.stdin.readline().strip())

intersection=list(set(D)&set(B))
intersection.sort()

print(len(intersection))
for i in range(0, len(intersection)):
    print(intersection[i])

