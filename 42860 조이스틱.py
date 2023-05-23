# 프로그래머스 42860 조이스틱
# AAAAAA -> JEROEN


def solution(name):
    answer = 0  # 조이스틱을 움직이는 횟수
    stringlen = len(name)
    name = list(name)
    Acount = []
    for i in range(len(name)):
        if ord(name[i]) > 77:
            answer += 91 - ord(name[i])
        else:
            answer += ord(name[i]) - 65
    # string을 아스키코드로 변환
    for i in range(stringlen):
        name[i] = ord(name[i])

    # A가 아닌 문자를 찾아서 조이스틱을 움직이는 횟수를 더해준다.
    for i in range(stringlen):
        if name[i] != 65:
            answer += min(name[i] - 65, 91 - name[i])
            answer += 1

    return answer - 1


# print(solution("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(solution("JEROEN"))
print(solution("JAN"))
# ABCDE FGHIJ KLMNO PQRST UVWXY Z
# 65 ~ 90
