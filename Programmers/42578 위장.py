# 2023.04.18

def solution(clothes):
    answer = 0
    dic = {}
    for a, b in clothes:
        if b not in dic:
            dic[b] = [a]
        else:
            dic[b].append(a)
    
    answer = 1
    for key in dic:
        answer *= (len(dic[key])+1)
    return answer - 1

solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
