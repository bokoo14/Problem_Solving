# 2023.01.05
from collections import deque

def solution(people, limit):
    answer = 0
    people=deque(sorted(people)) # 가벼운 ~ 무거운
    while len(people)>=2: # 보트에 남은 사람이 2명 이상일때
        if people[0]+people[-1] <= limit:
            people.pop()
            people.popleft()
            answer+=1
        else: 
            people.pop()
            answer+=1
    if people: # 마지막으로 보트에 1명만 남아있다면 
        answer+=1

    return answer