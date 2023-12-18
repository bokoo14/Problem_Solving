# 프로그래머스 42842번: 카펫


def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total + 1):
        if total % i == 0:
            a = i
            b = total // i
            if (a - 2) * (b - 2) == yellow:
                answer.append(b)
                answer.append(a)
                break
    return answer
