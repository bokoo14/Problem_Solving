# 2023.01.05
import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

totalDist = 10**9 # 최종 치킨 거리
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j]==1: # 집이면
            home.append([i, j])
        elif city[i][j]==2: # 치킨 집이면
            chicken.append([i, j])
        
for chick in combinations(chicken, m): # 여러 치킨집 중 m개를 선택해 가장 가까운 집사이의 거리 구하기
    answer = 0
    for homeX, homeY in home: # 모든 집 탐색 -> 치킨집과 가장 가까운 집 구하기
        distance = 10**9
        for j in range(m): # m개의 치킨 집 -> 현재 집~치킨 집사이의 거리 구하기
            distance = min(distance, abs(homeX-chick[j][0])+abs(homeY-chick[j][1]))
        answer+=distance
    totalDist = min(answer, totalDist)

print(totalDist)

