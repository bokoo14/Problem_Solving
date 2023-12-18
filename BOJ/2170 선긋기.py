# 2023.01.04
import sys
input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort(key = lambda x: (x[0], x[1])) # x좌표, y좌표 오름차순 정렬

answer=[[xy[0][0], xy[0][1]]]
index=0
for xx, yy in xy:
    if answer[index][1]>xx: # 현재 선이 이미 그은 선에 겹치면
        answer[index][1]=max(answer[index][1], yy) # 선을 연장시켜줌
    else: # 이미 그은 선과 겹치지 않으면 - 새로운 선분을 그을때
        answer.append([xx, yy])
        index+=1
 
total=0
for x, y in answer:
    total+=(y-x)
print(total)