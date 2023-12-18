import math

def solution(progresses, speeds):

    answer = [] # 각 배포마다 몇 개의 기능이 배포
    time = [0]* (len(progresses)) # 각각 걸리는 시간
    
    for i in range(len(progresses)):
        time[i] = math.ceil((100-progresses[i]) / speeds[i])
    # time: 7, 2, 9
    
    total = 1
    tmp = time.pop(0)
    while time:
        if time[0]<=tmp:
            time.pop(0)
            total+=1
        else:
            tmp = time.pop(0)
            answer.append(total)
            total = 1
    answer.append(total)
        
    return answer