# 2023.06.06
# 프로그래머스 43238 입국심사

"""
def solution(n, times):
    answer = 0
    times.sort()  # 이분탐색을 하려면 배열이 정렬되어 있어야 함
    first = 0
    end = times[-1] * n
    mid = (end) // 2  # 가장 시간이 오래 걸리는 것의 중간값

    while True:
        for i in range(n, 0, -1):  # n~1 까지
            if mid % i == 0:  # 나누어 떨어지는 경우
                answer = mid // i
                break
        if answer == n:
            break
        else:
            mid += 1

    return answer


print(solution(6, [7, 10]))
"""


# 이용준 풀이
def solution(n, times):
    def person(value):
        answer = 0
        for i in times:
            answer += value // i
        return answer

    start, end = 0, (n // len(times) + 1) * max(times)
    while start <= end:
        mid = start + (end - start) // 2
        value = person(mid)
        if value >= n:
            end = mid - 1
            if person(mid - 1) < n:
                return mid
        else:
            start = mid + 1


print(solution(6, [7, 10]))
