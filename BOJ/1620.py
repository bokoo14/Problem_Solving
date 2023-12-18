#1620
#2022.06.30

#readline은 엔터까지 받아줌
#strip()으로 앞뒤 공백 제거헤서 받아줌
#split은 리스트형태로 값 저장

'''
리스트 탐색 시간 복잡도 O(n)
딕셔너리, 해시 테이블 시간 복잡도 O(1)
https://trey-de.tistory.com/7
'''

import sys

N, M=map(int, sys.stdin.readline().split())

pocket={}
pocket_dic={}
for i in range(1, N+1):
    p=sys.stdin.readline().strip()
    pocket[i]=p
    pocket_dic[p]=i


for i in range(0, M):
    q=sys.stdin.readline().strip()
    #print(q)
    #print(len(q))
    if q.isdigit():
        print(pocket[int(q)])
    else:
        print(pocket_dic[q])
