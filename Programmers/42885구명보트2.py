# 2023.01.05
def solution(people, limit):
    answer = 0
    people.sort() # 몸무게 가벼운~무거운 
    left=0
    right=len(people)-1
    while left<right:
        if people[left]+people[right]<=limit: # 두 명이 한 보트를 탈때
            left+=1
            right-=1
            answer+=1
        else:
            right-=1
            answer+=1
    if left==right: # 마지막에 한명만 남게 되었다면 보트에 한명만 태움
        answer+=1

    return answer