

'''
# 2023.07.04
import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
'''

dp = [[0 for _ in range(3)] for _ in range(11)] #dp초기화

# 각각 1,2,3으로 끝나는 경우의 수
dp[1] = [1, 0, 0]
dp[2] = [1, 1, 0]
dp[3] = [2, 1, 1]

for i in range(4, 11):
    # 만약 i가 6일때

    # 5에서 1,2,3으로 끝난 경우들에 1을 더해주면 6이다.
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i-1][2]
    # 4에서 1,2,3으로 끝난 경우들에 2를 더해주면 6이다.
    dp[i][1] = dp[i - 2][0] + dp[i - 2][1] + dp[i-2][2]
    # 3에서 1,2,3으로 경우 들에 3을 더해주면 6이다.
    dp[i][2] = dp[i - 3][0] + dp[i - 3][1] + dp[i-3][2]
    
    #N이 6일때의 횟수
    print(sum(dp[6])