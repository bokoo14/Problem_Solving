# 2023.04.18
'''
def solution(participant, completion):
    answer = ""
    
    diff = set(participant) - set(completion)
    if len(diff)>0: # 동명이인이 없다면
        answer = list(diff)[0]
    else: # 동명이인이 있다면
        dic = {}
        for name in participant:
            if name not in dic:
                dic[name] = 1
            else:
                dic[name]+=1
        for name, count in dic.items():
            if count > 1:
                answer = name
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
'''

def solution(participant, completion):
    answer = ''
    dic = {}
    for a in participant:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
    for b in completion: # completion은 무조건 dic에 있으니까 
        dic[b] -= 1
    for key in dic: 
        if dic[key] == 1: # 딕셔너리에 남아있는 사람이 정답
            answer = key
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))



'''
def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    for i in range (len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]
'''