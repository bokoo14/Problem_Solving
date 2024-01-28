from itertools import *

def solution(k, dungeons):
    # k: 현재 피로도, dungeons: [최소 필요 피로도, 소모 피로도]
    answer = 0 # 탐험할 수 있는 최대 던전 수
    
    allDungeons = list(permutations(dungeons, len(dungeons))) # 모든 던전의 경우의 수

    for d in allDungeons:
        visitedDungeonsCount = 0
        currentK = k
        for x, y in list(d):
            if x <= currentK and y <= currentK: # 현재 남은 피로도가 최소 필요도보다 크고, 뺼 수 있으면?
                currentK -= y
                visitedDungeonsCount += 1
        # 모든 던전들을 탐험하고, 최대 던전 수 구하기
        answer = max(visitedDungeonsCount, answer)

    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))
