# 2023.12.14

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        intersectMap = str(format(arr1[i] | arr2[i], 'b').rjust(n, "0"))
        tmpString = ''
        for tmp in intersectMap:
            if tmp == '0':
                tmpString += " "
            else:
                tmpString += "#"
        answer.append(tmpString)

    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))