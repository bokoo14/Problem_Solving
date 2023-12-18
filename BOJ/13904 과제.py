# 2023.01.22
import sys
input = sys.stdin.readline

n = int(input()) # 과제의 수
homework = [list(map(int, input().split())) for _ in range(n)] # 남은 일수, 점수
homework.sort(key = lambda x: (-x[1], x[0]))
# 과제 점수가 가장 높은 순, 날짜 조금 남은 순으로 정렬
# [[4, 60], [2, 50], [4, 40], [3, 30], [1, 20], [4, 10], [6, 5]]

solved=[False]*(1001) # 1000개의 문제 -> index는 날짜를 나타냄
def greedy(homework):
    answer=0 # 총 과제의 점수
    for i in range(n): # 모든 과제를 검사해줌
        index=homework[i][0] # 과제남은 날짜
        while index>0: # 과제를 수행할 수 있는지 없는지 검사
            if solved[index]==False:
                solved[index]=True
                answer+=homework[i][1]
                break
            index-=1
    return answer

print(greedy(homework))