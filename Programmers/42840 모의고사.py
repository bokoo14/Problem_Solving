def solution(answers):
    answer = [] # 문제를 가장 많이 맞힌 사람
    # 문제를 찍는 경향
    oneP = [1, 2, 3, 4, 5] * (len(answers)//5 + 1)
    twoP = [2, 1, 2, 3, 2, 4, 2, 5]  * (len(answers)//8 + 1)
    threeP = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (len(answers)//10 + 1)
    
    # 채점
    solved1, solved2, solved3 = 0, 0, 0
    for index, a in enumerate(answers):
        if a == oneP[index]:
            solved1+=1
        if a == twoP[index]:
            solved2+=1
        if a == threeP[index]:
            solved3+=1
    solveProblemCount = max(solved1, max(solved2, solved3))
    
    if solved1 == solveProblemCount:
        answer.append(1)
    if solved2 == solveProblemCount:
        answer.append(2)
    if solved3 == solveProblemCount:
        answer.append(3)
    
    
    
    return answer