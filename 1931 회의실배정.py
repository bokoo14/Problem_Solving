# 2023.01.04
import sys
input = sys.stdin.readline

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]

time.sort(key=lambda x: (x[1], x[0]))
# print(time)
endtime = time[0][1] # 회의가 끝나는 시간
index=1
for i in range(1, n):
    if endtime <= time[i][0]:
        endtime = time[i][1]
        index+=1

print(index)
