#2529
#2022.07.27

'''
브루트포스 알고리즘, 백트래킹
-브루트포스: 완전탐색 알고리즘. 가능한 모든 경우의 수를 모두 탐색하면서 요구 조건에 충족되는 결과만을 가져온다
해가 존재할 것으로 예상되는 모든 영역을 전체 탐색하는 방법
순차 탐색, 깊이 우선 탐색, 너비 우선 탐색

-백트래킹: 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법
최적화 문제, 결정 문제를 푸는 방법
'''

import sys
from itertools import permutations

k=int(sys.stdin.readline())

array=list(sys.stdin.readline().split())

answer=[]
for num in permutations([0,1,2,3,4,5,6,7,8,9], k+1):
    okay=True
    for j in range(k):
        if array[j]=='<':
            if num[j]<num[j+1]:
                continue
            else:
                okay=False
                break
        elif array[j]=='>':
            if num[j]>num[j+1]:
                continue
            else:
                okay=False
                break

    if okay==True:
        answer.append(num)


print(''.join(map(str,list(max(answer)))))
print(''.join(map(str,list(min(answer)))))
