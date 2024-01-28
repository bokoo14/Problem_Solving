'''
미로 A에서 출발점은 A[0][0]이며 도착점은 A[N-1][M-1]이라 하자.
미로의 각 지점 A[i][j]를 지나갈 때 해당 지점의 값을 통행세로 내야한다.
미로의 각 지점에서는 오른쪽이나 아래쪽으로만 이동이 가능하다.
N*M 크기의 미로에서 내야 하는 통행세의 최소값을 출력하시오.
'''

import sys
input=sys.stdin.readline

n, m = map(int, input().split())
maze=[list(map(int, input().split())) for _ in range(n)]

# dp table
dp=[[0]*(m)]*(n)

def sol(n, m):
    for i in range(n):
        for j in range(m):
            if i==0 and j==0: # 시작
                dp[i][j]=maze[i][j]
            elif i==0: # 오른쪽으로만 이동
                dp[i][j]=maze[i][j]+dp[i][j-1]
            elif j==0: # 아래쪽으로만 이동
                dp[i][j]=maze[i][j]+dp[i-1][j]
            else: # 오른쪽 or 아래쪽으로 이동 중 최소값 저장
                dp[i][j]=maze[i][j]+min(dp[i-1][j], dp[i][j-1])

sol(n, m)
#print(dp)
print(dp[n-1][m-1])                
