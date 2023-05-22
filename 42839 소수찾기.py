import math
import itertools


# 소수 판별
def primenumber(x):
    for i in range(2, int(x**0.5 + 1)):  # 2부터 x의 제곱근까지의 숫자
        if x % i == 0:  # 나눠떨어지는 숫자가 있으면 소수가 아님
            return False
    return True  # 전부 나눠떨어지지 않는다면 소수임


def solution(numbers):
    answer = 0
    number = list(numbers)
    tmp = []
    for i in range(1, len(number) + 1):
        nPr = itertools.permutations(number, i)
        for i in nPr:
            permu = int("".join(list(i)))
            tmp.append(permu)

    tmp = list(set(tmp))
    print(tmp)
    for tt in tmp:
        if tt >= 2 and primenumber(tt):  # 소수라면 +1해줌
            answer += 1

    return answer


print(solution("011"))
