# 프로그래머스 42746 가장큰수

def solution(numbers):
   answer = ''
   numbers = list(map(str, numbers))
   numbers.sort(key=lambda x: x*3, reverse=True)
   answer = str(int(''.join(numbers)))
    
   return answer

print(solution([3, 30, 34, 5, 9]))


#[3, 30, 34, 5, 9] -> 333 303030 343434 555 999
#                  -> 999 555 343434 333 303030
#[9, 5, 34, 3, 30] "9534330"
'''
sort() 메소드에서 key 파라미터를 이용하여 각 요소를 3번 반복한 문자열의 크기를 기준으로 정렬하는 이유는, 
문제에서 제시된 조건인 "numbers의 원소는 0 이상 1,000 이하입니다"라는 제한 사항 때문입니다. 
'''
