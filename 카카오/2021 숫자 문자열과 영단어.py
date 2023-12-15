# 2023.12.14

numberString = {'zero': '0',
                'one': '1', 
                'two': '2', 
                'three': '3', 
                'four': '4', 
                'five': '5',
                'six': '6',
                'seven': '7', 
                'eight': '8',
                'nine': '9'}

def solution(s):
    answer = 0
    stringanswer = ''
    tmpword = ''
    for word in s:
        if ord(word)>=97 and ord(word)<=122: # 문자라면
            tmpword+=word
            if tmpword in numberString:
                stringanswer += numberString[tmpword]
                tmpword = ''
        else: # 숫자라면
            stringanswer += str(word)
            
    answer = int(stringanswer)
    return answer

print(solution('one4seveneight'))