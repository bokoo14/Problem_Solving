# 2023.05.22 큰 수 만들기


def solution(number, k):
    answer = ""
    number = list(map(int, list(number)))
    # k개의 수를 제거해야 함 -> k번 반복
    for i in range(k):
        tmp = min(number)
        for num in number:
            # 돌아가면서 가장 작은 숫자를 찾아줌
            if num < tmp:
                tmp = num

    return answer


print(solution("1924", 2))
