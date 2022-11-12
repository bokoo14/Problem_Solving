#12970 AB
#2022.08.10
'''
import sys
input=sys.stdin.readline
#문자열의 길이, K쌍
N, K = map(int, input().split())

def AB():
    #초기: 모두 B로 초기화 해줌
    a=0 #초기 A의 수
    b=N #초기 B의 수

    while a*b<K and b>0:
        a+=1 #A를 하나 증가
        b-=1 #B를 하나 증가

    if K==0:
        return 'B'*N
    elif b==0: #그러한 S가 존재하지 않는 경우 
        return -1

    remain = K-(a-1)*b #남아있는 쌍의 수??
    return 'A'*(a-1)+'B'*(b-remain)+'A'+'B'*remain

print(AB())
'''
#@authorized by 이태곤
N, K = map(int,input().split())
list = ['B' for _ in range(N)]    #리스트 모두 B로 초기화
flag = 0
for i in range(N):    #경우의 수 모두 검사
    list[i] = 'A'
    count = 0
    for j in range(0,len(list)-1):    #0부터 마지막인덱스 전까지 -> 마지막에 'A'가 위치해도 count = 0
        if list[j] == 'A':    #인덱스에 'A'가 위치해있으면
            for k in range(j+1, len(list)):    #'B'의 갯수만 카운트
                if list[k] == 'B':
                    count+=1
    if K == count:    #같으면
        flag = 1
        break
    elif K < count:    #count가 더 크다면 B로 돌려놓고 다음 분기문 실행
        list[i] = 'B'
if flag == 1: print("".join(list))    #일치해서 탈출한 경우
else: print(-1)    #만들어질 수 없는 경우 -1출력

