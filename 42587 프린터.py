# Programmers 42587 프린터

from collections import deque

def solution(priorities, location):
    answer = 0

    q = deque()
    for i in range(len(priorities)):
        q.append([priorities[i], i]) # [우선순위, 인덱스]

    while q:
        tmp = q.popleft()
        if q:
            if tmp[0] < max(q)[0]:
                q.append(tmp)
            else:
                answer+=1
                if tmp[1] == location:
                    break
        else:
            answer+=1
            break

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))



'''
# 워커의 좋은 풀이
def solution(priorities, location):
    answer = 0
    while True:
        max_num = max(priorities)
        for i in range(len(priorities)):
            if max_num == priorities[i]:
                answer += 1
                priorities[i]=0
                max_num = max(priorities)
                if i == location:
                    return answer

'''