def makeArrays(sstr): #"FRANCE", "aa1+aa2"  # 다중집합 만들기
    sstr = sstr.lower()
    sstr = list(sstr+ " ") # 문자열 한글자씩 끊기
    for i in range(len(sstr)-1):
        sstr[i] = sstr[i] + sstr[i+1]
    new_sstr = []
    for s in sstr:
        if len(s) == 2 and 97 <= ord(s[0]) <= 122 and 97 <= ord(s[1]) <= 122:
            new_sstr.append(s)
    return new_sstr

def findIntersect(str1, str2): # 교집합의 개수 구하기
    intersectArray = []
    for s1 in str1:
        if s1 in str2: # 두 집합의 원소가 동일하다면
            intersectArray.append(s1)
            str2.remove(s1)
    return len(intersectArray)

def solution(str1, str2):
    answer = 0
    # 다중집합 만들기
    str1 = makeArrays(str1)
    str2 = makeArrays(str2)
    
    # 교집합의 개수 구하기
    str1Len1, str2Len2 = len(str1), len(str2)
    numberOfIntersect = 0
    if str1Len1 <= str2Len2:
        numberOfIntersect = findIntersect(str1, str2)
    else:
        numberOfIntersect = findIntersect(str2, str1)
        
     # 자카드 유사도
    if len(str1) == 0 and len(str2) == 0:
        answer = 1 * 65536
    else: 
        answer = int(numberOfIntersect / (str1Len1+str2Len2-numberOfIntersect) * 65536)
    return answer


print(solution("handshake", "shake hands")) #65536
print(solution("aa1+aa2", "AAAA12")) #43690
print(solution("E=M*C^2", "e=m*c^2")) #65536
