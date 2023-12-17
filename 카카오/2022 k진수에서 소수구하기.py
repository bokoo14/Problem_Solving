import math

def decimalToK(num, k): # k진수로 변환
    kNum = ""
    while num > 0:
        kNum = str(num%k) + kNum
        num = num//k
    return kNum

def isPrimeNumber(num):
    if num < 2: # 2 이하의 수는 소수가 아님
        return False
    mid = int(math.sqrt(num))
    for i in range(2, mid+1):
        if num%i == 0: # 약수가 1과 자기자신이 아니라면 소수 아님
            return False
    return True
    
def solution(n, k):
    answer = 0
    kNum = decimalToK(n, k).split("0")
    
    for i in kNum:
        if i != '' and isPrimeNumber(int(i)):
            answer+=1
    return answer

print(solution(437674, 3)) # 211020101011 -> answer: 3
print(solution(110011, 10)) # answer: 2