# 2023.01.07
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split()) # 행, 열, 인벤토리
land = [list(map(int, input().split())) for _ in range(n)]

answer=10**9
for i in range(257): # 256층 모두를 검사
    use=0 # 사용한 블록
    get=0 # 가져온 블록
    for x in range(n):
        for y in range(m):
            if land[x][y]>i: # 현재의 층보다 더 높을때 -> 1번 연산
                get+=(land[x][y]-i)
            else: # 현재의 층보다 부족하거나 같을때 -> 2번 연산
                use+=(i-land[x][y])
        
    if use>get+b: # 답이 되지 않으면 층을 갱신해주지 않음
        continue

    time=(get*2)+use
    if time<=answer: # 
        answer=time
        level=i

print(answer, level)




            