# 84512 모음사전
import itertools


def solution(word):
    answer = 0
    alpha = ["A", "E", "I", "O", "U"]
    dic = []
    for i in range(1, len(alpha) + 1):
        dic += itertools.product(alpha, repeat=i)

    for i in range(len(dic)):
        dic[i] = "".join(list(dic[i]))
    dic.sort()
    # print(dic[0:20])
    """
    for i in range(len(dic)):
        if dic[i] == word:
            answer = i + 1
            break
    """
    answer = dic.index(word) + 1
    return answer


print(solution("AAAAE"))
