#1744 수 묶기
#2022.08.12
#그리디 알고리즘, 정렬
'''
핵심: 양수(1제외)
'''
import sys
input=sys.stdin.readline

N = int(input()) #수열의 길이 
array=[0]*(N)
for i in range(N):
    array[i]=int(input())

minus=[]
plus=[]
one=[]
for i in range(N):
    if array[i]==1:
        one.append(array[i])
    elif array[i]>1:
        plus.append(array[i])
    elif array[i]<=0:
        minus.append(array[i])

        
plus.sort(reverse=True) #양수(1제외)->내림차순 정렬(큰 순서)
minus.sort() #음수(0포함)->오름차순 정렬(작은 순서)
#------------------------------------------------------
answer=0
#양수(1제외)
if len(plus)%2==0:
    for i in range(0, len(plus), 2):
        answer+=(plus[i]*plus[i+1])
else:
    for i in range(0, len(plus)-1, 2):
        answer+=(plus[i]*plus[i+1])
    answer+=plus[len(plus)-1]

#음수
if len(minus)%2==0:
    for i in range(0, len(minus), 2):
        answer+=(minus[i]*minus[i+1])
else:
    for i in range(0, len(minus)-1, 2):
        answer+=(minus[i]*minus[i+1])
    answer+=minus[len(minus)-1]

#1 모두 더해주기
answer+=sum(one)
print(answer)










            
