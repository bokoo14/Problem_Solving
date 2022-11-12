#12904 A와 B
#2022.08.08
#그리디 알고리즘
'''
그리디 알고리즘: 각 단계마다 지금 당장 가장 좋은 방법만을 선택
지금의 선택이 앞으로 남은 선택들에 어떤 영향을 끼칠지 고려하지 않음

원래 연산) A:문자열의 뒤에 A 추가, B:문자열을 뒤집고 뒤에 B추가
역연산) A:문자열의 가장 뒤를 삭제, B:문자열을 뒤를 삭제하고 뒤집기
'''
import sys
input=sys.stdin.readline

#S->T
S=list(input().strip())
T=list(input().strip())

while T:
    if T[-1]=='A':
        T.pop()
    elif T[-1]=='B':
        T.pop()
        T.reverse()
        
    if S==T:
        print(1)
        exit()

print(0)
