# 2023.04.18

def solution(nums):
    answer = 0
    number = len(nums)//2
    dic = {}
    for a in nums:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a]+=1
            
    if len(dic)>=number:
        answer = number
    else:
        answer = len(dic)
    return answer

'''
def solution(nums):
    return min(len(nums) // 2, len(list(set(nums))))
'''