def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a, b, c = commands[i][0], commands[i][1], commands[i][2]
        tmp = array[a-1:b] # 배열 자르기
        
        sorttmp = sorted(tmp) # 배열 정렬 -> 원본 배열은 건들지 않고 새로운 배열에 저장
        answer.append(sorttmp[c-1]) # k번째 값
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# 5, 2, 6, 3
