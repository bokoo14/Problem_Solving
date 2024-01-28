'''
개구리가 계단 아래 시작점부터 계단 꼭대기에 위치한 도착점까지 점프하는 게임을 하려고 한다.
개구리는 한 계단을 점프해서 오를 수도 있고, 두 계단을 점프해서 오를 수도 있다.
각 계단에는 일정한 점수가 부여되어 있으므로, 개구리가 계단을 밟으면 그 계단의 점수를 획득한다.
예를 들어, 아래 그램에서 개구리가, 첫 번째, 두 번째, 네 번째, 여섯 번째 계단을 밟아 도착점에 도달하면
개구리가 획득하는 점수는 10 + 20 + 25 + 20 = 75점이 된다.

N개의 계단에 부여된 점수가 주어질 때, 개구리가 획득할 수 있는 최대 점수를 출력하시오.
'''

import sys
input=sys.stdin.readline

n = int(input())
step=list(map(int, input().split()))

dp=[0]*(n)
dp[0]=step[0]
dp[1]=max(step[0]+step[1], step[1])
for i in range(2, n):
    dp[i]=step[i]+max(dp[i-1], dp[i-2])


print(dp[n-1])


# 백준 2579
'''
n=int(sys.stdin.readline()) #계단 수

#계단의 점수
step=[0]*(n+2)
for i in range(0, n):
    step[i]=int(sys.stdin.readline())

dp=[0]*(n+2)
dp[0]=step[0] 
dp[1]=step[0]+step[1]
dp[2]=max(step[0]+step[2], step[1]+step[2])

for i in range(3, n):
    dp[i]=max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])    

print(dp[n-1])​

'''
