# 2023.04.11
def solution(arr):
    answer = []
    tmp = 10**9
    for i in arr:
        if tmp!=i:
            answer.append(i)
            tmp = i
            
    return answer