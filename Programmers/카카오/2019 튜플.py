def solution(s):
    answer = []
    s = s[1:len(s)-2]
    s = s.split("}")
    for i in range(len(s)):
        if s[i][0]==",":
            s[i] = s[i][2:]
        elif s[i][0]=="{":
            s[i] = s[i][1:]
    s.sort(key=len)

    for i in range(len(s)):
        tmp = s[i].split(",")
        tmp2 = set(tmp) - set(answer)
        answer.append(*tmp2)

    for i in range(len(answer)):
        answer[i] = int(answer[i])
    return answer

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
