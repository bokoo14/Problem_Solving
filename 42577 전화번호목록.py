# 2023.04.18
'''
def solution(phone_book):
    answer = True # 접두어가 없으면 true
    phone_book.sort()
    print(phone_book)
    length = len(phone_book)

    for i in range(length - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            break
    return answer

#solution(["119", "97674223", "1195524421"])
#solution(["12","123","1235","567","88"])

solution(["1", "12312", "1234", "23", "234", "256", "2", "1232", "36", "3", "32"])

'''
'''
파이썬의 정렬 기준 - 문자열 ㄴsort
이때, 문자열의 첫 번째 글자부터 ASCII 값으로 비교하면서 정렬을 수행합니다. 따라서, 위의 결과에서는 '1232'가 '12312'보다 먼저 나오는 것을 확인할 수 있습니다.

만약, 숫자로 정렬하고 싶다면, sort() 메소드의 key 인자를 활용하여 정렬 기준을 지정할 수 있습니다. 
예를 들어, solution(["1", "12312", "1234", "23", "234", "256", "2", "1232", "36", "3", "32"], key=int)와 같이 key 인자에 int 함수를 넣으면, 
숫자로 정렬할 수 있습니다. 이때, int 함수는 문자열을 정수로 변환하는 함수입니다.
'''


a = ["123445", "123"]

b = "12"
c = b[:4]
print(b)
print(c)
