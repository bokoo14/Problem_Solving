# 2023.01.07
import sys
input = sys.stdin.readline

t = int(input()) # test case
for i in range(t):
    n, m = map(int, input().split())
    number = list(map(int, input().split()))
    index=0
    answer=0 # 프린트해주면 +1씩 증가
    while 1:
        if max(number)==number[index]: # 현재 index의 값이 가장 큰 값이라면?
            answer+=1 # 프린트해줌
            if index==m: # 현재 index의 값이 가장 큰 값이고, 찾는 값이라면?
                print(answer)
                break
            else: # 찾는 값이 아니라면?
                number[index]=-1 # -1을 대입
                index=(index+1)%n
        else: # 가장 큰 값이 아니라면 큐의 제일 뒤로 
            index=(index+1)%n
