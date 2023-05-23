# 2023.05.22 큰 수 만들기

"""
def solution(number, k):
    answer = ""
    number = list(map(int, list(number)))
    # k개의 수를 제거해야 함 -> k번 반복
    for i in range(k):
        tmp = min(number)
        for num in number:
            # 처음부터 돌아가면서 가장 작은 숫자를 찾아서 제거해줌
            if num == tmp:
                number.remove(num)
                break
    # 글자 합치기
    for j in number:
        answer += str(j)
    return answer


print(solution("1231234", 3))
"""

"""
def solution(number, k):
    answer = []

    for i in number:
        if not answer:
            answer.append(i)
            continue
        while answer[-1] < i and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        answer.append(i)
        if len(answer) == len(number) - k:
            break
    return "".join(answer)


print(solution("1231234", 3))
print(solution("4177252841", 4))
"""


def solution(number, k):
    answer = []  # 글자를 담을 배열
    number = list(map(int, list(number)))

    for num in number:
        if len(answer) == 0:
            answer.append(num)
        while k>=0 and answer 
    return answer


# print(solution("4177252841", 4))
solution("1231234", 4)  # 3234
solution("4177252841", 4)  # 775841
