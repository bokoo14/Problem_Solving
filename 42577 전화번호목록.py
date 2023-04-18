# 2023.04.18
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