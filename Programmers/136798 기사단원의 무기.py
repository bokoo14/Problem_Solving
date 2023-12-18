def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        tmp = 0
        # 해당 수의 약수의 개수를 count
        for j in range(1, int(i**0.5)+1):
            if i%j == 0: # 약수라면
                if j == i//j: # 제곱근이라면
                    tmp += 1
                else: # 제곱근이 아닐 경우
                    tmp += 2 
        if tmp > limit:
            answer += power
        else:
            answer += tmp
    return answer