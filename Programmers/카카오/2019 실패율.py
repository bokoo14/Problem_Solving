def findFailRatio(target, stages):
    reachCount = 0
    for s in stages:
        if s >= target:
            reachCount += 1
    return reachCount
    
def solution(N, stages):
    answer = []
    tmp = []
    for i in range(N):
        if i+1 not in tmp:
            reachCount = findFailRatio(i+1, stages)
            if reachCount == 0:
                tmp.append([i+1, 0])
            else:
                tmp.append([i+1, stages.count(i+1)/reachCount])
    tmp.sort(key = lambda x: (-x[1], x[0]))
    
    for a, b in tmp:
        answer.append(a)
        
    return answer