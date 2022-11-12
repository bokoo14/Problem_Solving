#1931
#2022.07.26

'''
그리디 알고리즘, 정렬
가장 빨리 끝나는 일을 기준으로 선택
빨리 끝날수록 뒤에 고려해볼 회의가 많기 때문

정렬 순서
1. 시작하는 시간의 오름차순
2. 끝나는 시간의 오름차순
=> 끝나는 시간을 기준으로 정렬이 됨

그리디 알고리즘이라서 1, 2 순으로 둘 다 정렬해주어야 함
'''

import sys

N=int(sys.stdin.readline())

#N행 2열
meeting=[[] for _ in range(N)]
for i in range(0, N):
    a, b= map(int, sys.stdin.readline().split())
    meeting[i].append(a)
    meeting[i].append(b)


meeting.sort(key=lambda x:x[0])
meeting.sort(key=lambda x:x[1])

answer=[]
answer.append(meeting[0])
k=0
for i in range(1, N):
    if answer[k][1]<=meeting[i][0]:
        answer.append(meeting[i])
        k+=1

print(len(answer))
