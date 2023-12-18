#1783 병든 나이트
import sys
input=sys.stdin.readline

#세로, 가로
N, M = map(int, input().split()) 

if N ==1:
    print(1)
elif N ==2: #2, 3만 쓸 수 있음
       print(min(4, (M+1)//2))
else: 
    if M<7: #1, 4만 쓰는게 제일 좋음(이동 횟수가 4보다 적은 경우))
        print(min(4, M))
    else: #1, 2, 3, 4를 모두 쓰고 ->1, 4만 쓰는게 좋음
        print(5+(M-7))

    
