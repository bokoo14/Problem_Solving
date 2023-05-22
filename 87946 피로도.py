#   Programmers87946 완전탐색 피로도

import itertools


# 유저의 현재 피로도, 최소 필요 피로도, 소모 피로도
def solution(k, dungeons):
    answer = -1
    l = list(itertools.permutations(dungeons, len(dungeons)))

    # print(l)
    # 모든 경우의 수를 다 탐색
    for i in l:
        tmp = k
        """
        for j in range(len(l)):
            if k>=
        """
    return answer


print(solution(80, [[80, 20], [50, 40], [30, 10]]))
