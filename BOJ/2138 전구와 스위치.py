# 2138 전구와 스위치
#2022.08.06
#그리디 알고리즘
import sys
input=sys.stdin.readline

N = int(input()) #N개의 스위치, N개의 전구
current=list(map(int, input().strip())) #현재 상태
final=list(map(int, input().strip())) #만들고자 하는 상태

cnt=0
for i in range(N):
    if current==final:
        print(cnt)
        break
    
    if i==0:
        current[i] = int(not current[i])
        current[i+1] = 1-current[i+1]
        cnt+=1
    elif i==N-1:
        current[i] = 1-current[i]
        current[i-1] = 1- current[i-1]
        cnt+1
    else:
        current[i-1] = 1-current[i-1]
        current[i] = 1-current[i]
        current[i+1] = 1-current[i+1]
        cnt+=1

if current!=final:
    print(-1)
        


        
