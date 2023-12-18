def solution(n, lost, reserve):
    answer = 0
    # 학생들 - 도난: 0, 여분: 2, 있는: 1
    student = [1] * (n + 2)
    student[0], student[n + 1] = -1, -1

    # 여분 있는 아이들을 check
    for resS in reserve:
        student[resS] = 2
    # 도난 당한 아이들을 check
    for lostS in lost:
        if student[lostS] == 2:
            student[lostS] = 1
        else:
            student[lostS] = 0

    # print(student)
    # 여분이 있는 아이들을 기준으로 앞 뒤 아이들에게 빌려줄 수 있을지 없을지 판단
    reserve.sort()
    for i in reserve:
        # 지금 체육복을 빌려줄 수 있을지 check
        if student[i] == 2:
            # 앞 뒤로 도난당했는지 check
            if student[i - 1] == 0:
                student[i - 1] = 1
                student[i] = 1
            elif student[i + 1] == 0:
                student[i + 1] = 1
                student[i] = 1

    # 수업을 들을 수 있는 학생 check
    for i in range(1, len(student)):
        if student[i] == 1 or student[i] == 2:
            answer += 1
    return answer


# 전체, 도난, 여벌
# 앞 뒤의 아이에게 빌려줄 수 있음
print(solution(5, [2, 4], [1, 3, 5]))
# print(solution(3, [3], [1]))
