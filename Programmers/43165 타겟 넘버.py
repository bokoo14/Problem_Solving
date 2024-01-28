# 2023.05.30
# 프로그래머스 43165 타겟넘버.py

from collections import deque


# def solution(numbers, target):
#     answer = 0
#     q = deque()
#     q.append([numbers[0], 0])  # 더하기
#     q.append([-numbers[0], 0])  # 빼기
#     while q:
#         temp, idx = q.popleft()
#         idx += 1
#         if idx < len(numbers):  # 연산의 횟수는 len(numbers)-1 까지만
#             q.append([temp + numbers[idx], idx])
#             q.append([temp - numbers[idx], idx])
#         else:  # 연산의 횟수를 초과했으면
#             if temp == target:  # 타겟 넘버를 만드는 방법 중 한가지라면
#                 answer += 1

#     return answer
from collections import deque

def solution(numbers, target):
    answer = 0 # 가능한 방법의 수
    stack = deque()
    stack.append([numbers[0], 0]) # 초기값 -> 더하기, 빼기
    stack.append([-numbers[0], 0])
    
    while stack:
        num, calNum = stack.popleft()
        if calNum < len(numbers)-1:
            stack.append([num+numbers[calNum+1], calNum+1]) # 더하기
            stack.append([num-numbers[calNum+1], calNum+1]) # 빼기
        else:
            if num == target:
                answer += 1
    return answer

print(solution([1, 1, 1, 1, 1], 3))
